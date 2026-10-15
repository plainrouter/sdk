import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { dirname } from 'node:path';

// Request selectors are derived from the signed contract, never response models.
const [output, input = new URL('../spec/openapi.json', import.meta.url)] = process.argv.slice(2);
if (!output) throw new Error('usage: generate-integer-fields.mjs OUTPUT [SPEC]');
const spec = JSON.parse(await readFile(input, 'utf8'));
const resolve = (value) => {
  if (!value?.$ref) return value;
  if (!value.$ref.startsWith('#/')) throw new Error(`Unsupported reference: ${value.$ref}`);
  return value.$ref.slice(2).split('/').reduce(
    (node, key) => node[key.replaceAll('~1', '/').replaceAll('~0', '~')], spec,
  );
};
const integerPaths = (schema, prefix = [], ancestors = new Set()) => {
  if (!schema || ancestors.has(schema)) return [];
  const seen = new Set(ancestors).add(schema);
  if (schema.$ref) return integerPaths(resolve(schema), prefix, seen);
  const types = Array.isArray(schema.type) ? schema.type : [schema.type];
  const paths = types.includes('integer') ? [prefix] : [];
  for (const [name, property] of Object.entries(schema.properties ?? {})) {
    paths.push(...integerPaths(property, [...prefix, name], seen));
  }
  if (schema.items) paths.push(...integerPaths(schema.items, [...prefix, '*'], seen));
  if (schema.additionalProperties && typeof schema.additionalProperties === 'object') {
    paths.push(...integerPaths(schema.additionalProperties, [...prefix, '*'], seen));
  }
  for (const kind of ['allOf', 'anyOf', 'oneOf']) {
    for (const branch of schema[kind] ?? []) paths.push(...integerPaths(branch, prefix, seen));
  }
  return paths;
};
const unique = (paths) => [...new Map(paths.map((path) => [JSON.stringify(path), path])).values()];
const operations = {};
for (const [path, rawItem] of Object.entries(spec.paths)) {
  const item = resolve(rawItem);
  for (const method of ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']) {
    const operation = item[method];
    if (!operation) continue;
    const fields = { operationId: operation.operationId, body: [], query: [], path: [] };
    const parameters = new Map();
    for (const raw of [...(item.parameters ?? []), ...(operation.parameters ?? [])]) {
      const parameter = resolve(raw);
      parameters.set(`${parameter.in}:${parameter.name}`, parameter);
    }
    for (const parameter of parameters.values()) {
      if (!['path', 'query'].includes(parameter.in)) continue;
      if (integerPaths(parameter.schema).some((selector) => selector.every((part) => part === '*'))) {
        fields[parameter.in].push(parameter.name);
      }
    }
    const body = resolve(operation.requestBody);
    for (const media of Object.values(body?.content ?? {})) {
      fields.body.push(...integerPaths(media.schema));
    }
    fields.body = unique(fields.body);
    operations[`${method.toUpperCase()} ${path}`] = fields;
  }
}
await mkdir(dirname(output), { recursive: true });
const json = JSON.stringify(operations, null, 2);
await writeFile(output, output.endsWith('.ts')
  ? `// Generated from spec/openapi.json by scripts/generate-integer-fields.mjs.\nexport const integerFields = ${json} as const;\n`
  : `${json}\n`);
