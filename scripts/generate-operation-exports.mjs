import { execFileSync } from 'node:child_process';
import { readFileSync, writeFileSync } from 'node:fs';
import ts from 'typescript';

const sourcePath = new URL('../packages/sdk/src/generated/sdk.gen.ts', import.meta.url);
const outputPath = new URL('../packages/sdk/src/operation-exports.ts', import.meta.url);
const specPath = new URL('../spec/openapi.json', import.meta.url);
const source = ts.createSourceFile(sourcePath.pathname, readFileSync(sourcePath, 'utf8'), ts.ScriptTarget.Latest, true);
const spec = JSON.parse(readFileSync(specPath, 'utf8'));
const names = [];
const declarations = new Map();

for (const statement of source.statements) {
  if (!statement.modifiers?.some((modifier) => modifier.kind === ts.SyntaxKind.ExportKeyword)) continue;
  if (ts.isVariableStatement(statement)) {
    for (const declaration of statement.declarationList.declarations) {
      if (!ts.isIdentifier(declaration.name)) throw new Error('Expected a named generated operation');
      names.push(declaration.name.text);
      declarations.set(declaration.name.text, declaration.initializer);
    }
  } else if (ts.isFunctionDeclaration(statement) && statement.name) {
    names.push(statement.name.text);
  }
}

if (!names.length) throw new Error('No generated operations found');

const resolve = (ref) => ref.slice(2).split('/').reduce(
  (node, key) => node[key.replaceAll('~1', '/').replaceAll('~0', '~')],
  spec,
);
const componentName = (ref) => typeof ref === 'string' && ref.startsWith('#/components/schemas/')
  ? ref.slice('#/components/schemas/'.length).replaceAll('~1', '/').replaceAll('~0', '~')
  : undefined;
const toRequestObjectSchema = (schema, seen = new Set()) => {
  if (!schema || typeof schema !== 'object') return {};
  if (schema.$ref) {
    if (seen.has(schema.$ref)) return {};
    return toRequestObjectSchema(resolve(schema.$ref), new Set(seen).add(schema.$ref));
  }

  const result = {};
  if (schema.additionalProperties === false) result.closed = true;
  if (schema.enum) result.enum = schema.enum;
  if (Object.hasOwn(schema, 'const')) result.const = schema.const;
  if (schema.properties) {
    result.properties = Object.fromEntries(Object.entries(schema.properties).map(([key, property]) => (
      [key, toRequestObjectSchema(property, seen)]
    )));
  }
  if (schema.items) result.items = toRequestObjectSchema(schema.items, seen);
  if (schema.anyOf) result.anyOf = schema.anyOf.map((branch) => toRequestObjectSchema(branch, seen));
  if (schema.oneOf) result.oneOf = schema.oneOf.map((branch) => toRequestObjectSchema(branch, seen));
  if (schema.allOf) result.allOf = schema.allOf.map((branch) => toRequestObjectSchema(branch, seen));
  if (schema.additionalProperties && typeof schema.additionalProperties === 'object') {
    result.additionalProperties = toRequestObjectSchema(schema.additionalProperties, seen);
  }

  return result;
};
const containsClosedObject = (schema) => (
  schema.closed === true
  || Object.values(schema.properties ?? {}).some(containsClosedObject)
  || (typeof schema.additionalProperties === 'object' && containsClosedObject(schema.additionalProperties))
  || Boolean(schema.items && containsClosedObject(schema.items))
  || (schema.anyOf ?? []).some(containsClosedObject)
  || (schema.oneOf ?? []).some(containsClosedObject)
  || (schema.allOf ?? []).some(containsClosedObject)
);
const referencedSchemas = (value, references = new Set(), visited = new Set()) => {
  if (!value || typeof value !== 'object') return references;
  if (value.$ref) {
    const name = componentName(value.$ref);
    if (name) references.add(name);
    if (visited.has(value.$ref)) return references;
    visited.add(value.$ref);
    return referencedSchemas(resolve(value.$ref), references, visited);
  }
  for (const child of Object.values(value)) referencedSchemas(child, references, visited);
  return references;
};
const dereference = (value) => {
  const seen = new Set();
  while (value?.$ref && !seen.has(value.$ref)) {
    seen.add(value.$ref);
    value = resolve(value.$ref);
  }
  return value;
};
const rootSchemaName = (schema, fallback) => componentName(schema?.$ref) ?? fallback;
const referencesActionProposal = (value, seen = new Set()) => {
  if (!value || typeof value !== 'object') return false;
  if (value.$ref) {
    if (value.$ref === '#/components/schemas/ActionProposalInput') return true;
    if (seen.has(value.$ref)) return false;
    return referencesActionProposal(resolve(value.$ref), new Set(seen).add(value.$ref));
  }
  return Object.values(value).some((child) => referencesActionProposal(child, seen));
};
const operationName = (operationId) => operationId
  .split(/[._-]+/)
  .filter(Boolean)
  .map((part, index) => index === 0
    ? `${part[0]?.toLowerCase() ?? ''}${part.slice(1)}`
    : `${part[0]?.toUpperCase() ?? ''}${part.slice(1)}`)
  .join('');
const actionOperations = new Map();
for (const item of Object.values(spec.paths)) {
  for (const [method, operation] of Object.entries(item)) {
    if (!['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace'].includes(method)) continue;
    if (!referencesActionProposal(operation.requestBody)) continue;
    actionOperations.set(operationName(operation.operationId), operation);
  }
}

const specializedExports = [];
const actionDataTypes = [];
for (const name of actionOperations.keys()) {
  const initializer = declarations.get(name);
  if (!initializer || !ts.isArrowFunction(initializer)) {
    throw new Error(`ActionProposalInput operation ${name} was not generated`);
  }
  const optionsType = initializer.parameters[0]?.type;
  const dataType = optionsType && ts.isTypeReferenceNode(optionsType)
    ? optionsType.typeArguments?.[0]
    : undefined;
  const typeParameter = initializer.typeParameters?.[0];
  if (!dataType || !typeParameter || initializer.typeParameters?.length !== 1) {
    throw new Error(`Could not read generated options/return generics for ${name}`);
  }
  const dataTypeName = dataType.getText(source);
  const throwName = typeParameter.name.text;
  actionDataTypes.push(dataTypeName);
  specializedExports.push(
    `export const ${name} = <${typeParameter.getText(source)}, const TBody extends ${dataTypeName}['body'] = ${dataTypeName}['body']>(options: Options<${dataTypeName}, ${throwName}> & { body: TBody & ExactActionProposal<TBody> }): ReturnType<typeof generated.${name}<${throwName}>> => operations.${name}(options as never);\n`,
  );
}

const specializedByName = new Map([...actionOperations.keys()].map((name, index) => [name, specializedExports[index]]));
const imports = actionOperations.size
  ? `import * as generated from './generated/sdk.gen.js';\nimport type { Options } from './generated/sdk.gen.js';\nimport type { ${[...new Set(actionDataTypes)].join(', ')} } from './generated/types.gen.js';\nimport type { ExactActionProposal } from './exact-action-params.js';\n`
  : '';
const output = '// Automatically derived from sdk.gen.ts and spec/openapi.json; do not edit.\n'
  + "import { operations } from './operations.js';\n"
  + imports
  + '\n'
  + names.map((name) => specializedByName.get(name) ?? `export const ${name} = operations.${name};\n`).join('');
let previous;
try {
  previous = readFileSync(outputPath, 'utf8');
} catch (error) {
  if (error.code !== 'ENOENT') throw error;
}
if (output !== previous) writeFileSync(outputPath, output);

const zodPath = new URL('../packages/sdk/src/generated/zod.gen.ts', import.meta.url);
const zodSource = ts.createSourceFile(zodPath.pathname, readFileSync(zodPath, 'utf8'), ts.ScriptTarget.Latest, true);
const zodNames = new Set();
for (const statement of zodSource.statements) {
  if (!statement.modifiers?.some((modifier) => modifier.kind === ts.SyntaxKind.ExportKeyword)) continue;
  if (!ts.isVariableStatement(statement)) continue;
  for (const declaration of statement.declarationList.declarations) {
    if (ts.isIdentifier(declaration.name)) zodNames.add(declaration.name.text);
  }
}

const closedRequestSchemas = new Map();
const requestBodyRoots = [];
for (const item of Object.values(spec.paths)) {
  for (const [method, operation] of Object.entries(item)) {
    if (!['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace'].includes(method)) continue;
    const requestBody = dereference(operation.requestBody);
    if (!requestBody?.content) continue;
    for (const [mediaType, media] of Object.entries(requestBody.content)) {
      if (!mediaType.toLowerCase().includes('json') || !media?.schema) continue;
      const schema = media.schema;
      const operationZodName = `z${operationName(operation.operationId)[0]?.toUpperCase() ?? ''}${operationName(operation.operationId).slice(1)}Body`;
      if (zodNames.has(operationZodName)) {
        requestBodyRoots.push({ name: operationZodName, schema });
      }
      for (const reference of referencedSchemas(schema)) {
        const name = `z${reference}`;
        if (zodNames.has(name)) {
          closedRequestSchemas.set(name, {
            rootName: reference,
            schema: spec.components.schemas[reference],
          });
        }
      }
    }
  }
}
for (const { name, schema } of requestBodyRoots) {
  closedRequestSchemas.set(name, {
    rootName: rootSchemaName(schema, name.slice(1)),
    schema,
  });
}

const requestZodPath = new URL('../packages/sdk/src/generated/request-zod.gen.ts', import.meta.url);
const wrappedRequestSchemas = [...closedRequestSchemas.entries()].flatMap(([name, entry]) => {
  const schema = toRequestObjectSchema(entry.schema);
  return containsClosedObject(schema) ? [[name, { ...entry, schema }]] : [];
});
const requestZodOutput = '// Automatically derived from spec/openapi.json and zod.gen.ts; do not edit.\n'
  + "import * as generated from './zod.gen.js';\n"
  + "import { withClosedRequestObjects, type RequestObjectSchema } from '../request-object-validation.js';\n\n"
  + wrappedRequestSchemas.map(([name, entry]) => (
    `export const ${name} = withClosedRequestObjects(${JSON.stringify(entry.rootName)}, ${JSON.stringify(entry.schema)} as const satisfies RequestObjectSchema, generated.${name});\n`
  )).join('');
let previousRequestZod;
try {
  previousRequestZod = readFileSync(requestZodPath, 'utf8');
} catch (error) {
  if (error.code !== 'ENOENT') throw error;
}
if (requestZodOutput !== previousRequestZod) writeFileSync(requestZodPath, requestZodOutput);

const zodExportsPath = new URL('../packages/sdk/src/generated/zod-exports.gen.ts', import.meta.url);
const zodExportNames = wrappedRequestSchemas.map(([name]) => name);
const zodExportsOutput = '// Automatically derived from spec/openapi.json and zod.gen.ts; do not edit.\n'
  + "export * from './zod.gen.js';\n"
  + (zodExportNames.length > 0
    ? `export { ${zodExportNames.join(', ')} } from './request-zod.gen.js';\n`
    : '');
let previousZodExports;
try {
  previousZodExports = readFileSync(zodExportsPath, 'utf8');
} catch (error) {
  if (error.code !== 'ENOENT') throw error;
}
if (zodExportsOutput !== previousZodExports) writeFileSync(zodExportsPath, zodExportsOutput);

execFileSync(process.execPath, [
  new URL('./generate-integer-fields.mjs', import.meta.url).pathname,
  new URL('../packages/sdk/src/generated/integer-fields.gen.ts', import.meta.url).pathname,
], { stdio: 'inherit' });
