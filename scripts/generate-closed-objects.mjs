import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { dirname } from 'node:path';

const [output, input = new URL('../spec/openapi.json', import.meta.url)] = process.argv.slice(2);
if (!output) throw new Error('usage: generate-closed-objects.mjs OUTPUT [SPEC]');
const spec = JSON.parse(await readFile(input, 'utf8'));
const schemas = {};
const escape = (value) => value.replaceAll('~', '~0').replaceAll('/', '~1');
const resolve = (pointer) => {
  if (!pointer.startsWith('#/')) throw new Error(`Unsupported reference: ${pointer}`);
  return pointer.slice(2).split('/').reduce(
    (node, key) => node[key.replaceAll('~1', '/').replaceAll('~0', '~')], spec,
  );
};
// Retain the request schema graph, including union discriminants. Response schemas
// never participate in request validation or model construction checks.
const visit = (schema, pointer) => {
  if (Object.hasOwn(schemas, pointer)) return pointer;
  const node = {};
  schemas[pointer] = node;
  if (schema.$ref) {
    node.$ref = visit(resolve(schema.$ref), schema.$ref);
    return pointer;
  }
  for (const key of ['type', 'title', 'required', 'enum', 'const', 'nullable']) {
    if (Object.hasOwn(schema, key)) node[key] = schema[key];
  }
  if (schema.properties) {
    node.properties = Object.fromEntries(Object.entries(schema.properties).map(([name, child]) => [
      name, { $ref: visit(child, `${pointer}/properties/${escape(name)}`) },
    ]));
  }
  for (const key of ['items', 'additionalProperties']) {
    if (!Object.hasOwn(schema, key)) continue;
    node[key] = typeof schema[key] === 'object'
      ? { $ref: visit(schema[key], `${pointer}/${key}`) }
      : schema[key];
  }
  for (const kind of ['allOf', 'anyOf', 'oneOf']) {
    if (schema[kind]) node[kind] = schema[kind].map((child, index) => ({
      $ref: visit(child, `${pointer}/${kind}/${index}`),
    }));
  }
  return pointer;
};
const operations = {};
for (const [path, item] of Object.entries(spec.paths)) {
  for (const method of ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']) {
    const operation = item[method];
    if (!operation?.requestBody) continue;
    const body = operation.requestBody.$ref ? resolve(operation.requestBody.$ref) : operation.requestBody;
    const bodyPointer = operation.requestBody.$ref ?? `#/paths/${escape(path)}/${method}/requestBody`;
    for (const [media, content] of Object.entries(body.content ?? {})) {
      if (!content.schema) continue;
      const pointer = visit(content.schema, `${bodyPointer}/content/${escape(media)}/schema`);
      // Every currently vendored operation has one body schema. Fail closed if a
      // future operation gives different schemas for different media types.
      if (operations[`${method.toUpperCase()} ${path}`] && operations[`${method.toUpperCase()} ${path}`] !== pointer) {
        throw new Error(`Multiple body schemas for ${operation.operationId}`);
      }
      operations[`${method.toUpperCase()} ${path}`] = pointer;
    }
  }
}
await mkdir(dirname(output), { recursive: true });
await writeFile(output, `${JSON.stringify({ schemas, operations }, null, 2)}\n`);
