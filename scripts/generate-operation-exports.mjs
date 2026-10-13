import { readFileSync, writeFileSync } from 'node:fs';
import ts from 'typescript';

const sourcePath = new URL('../packages/sdk/src/generated/sdk.gen.ts', import.meta.url);
const outputPath = new URL('../packages/sdk/src/operation-exports.ts', import.meta.url);
const source = ts.createSourceFile(sourcePath.pathname, readFileSync(sourcePath, 'utf8'), ts.ScriptTarget.Latest, true);
const names = [];

for (const statement of source.statements) {
  if (!statement.modifiers?.some((modifier) => modifier.kind === ts.SyntaxKind.ExportKeyword)) continue;
  if (ts.isVariableStatement(statement)) {
    for (const declaration of statement.declarationList.declarations) {
      if (!ts.isIdentifier(declaration.name)) throw new Error('Expected a named generated operation');
      names.push(declaration.name.text);
    }
  } else if (ts.isFunctionDeclaration(statement) && statement.name) {
    names.push(statement.name.text);
  }
}

if (!names.length) throw new Error('No generated operations found');
const output = '// Automatically derived from sdk.gen.ts; do not edit.\n'
  + "import { operations } from './operations.js';\n\n"
  + names.map((name) => `export const ${name} = operations.${name};\n`).join('');
let previous;
try {
  previous = readFileSync(outputPath, 'utf8');
} catch (error) {
  if (error.code !== 'ENOENT') throw error;
}
if (output !== previous) writeFileSync(outputPath, output);
