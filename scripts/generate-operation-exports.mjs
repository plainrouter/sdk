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

execFileSync(process.execPath, [
  new URL('./generate-integer-fields.mjs', import.meta.url).pathname,
  new URL('../packages/sdk/src/generated/integer-fields.gen.ts', import.meta.url).pathname,
], { stdio: 'inherit' });
