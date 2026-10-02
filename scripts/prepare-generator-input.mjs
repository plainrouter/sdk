import { readFile, writeFile } from 'node:fs/promises';

const [input, output] = process.argv.slice(2);
if (!input || !output) {
  throw new Error('usage: prepare-generator-input.mjs INPUT OUTPUT');
}

const contract = JSON.parse(await readFile(input, 'utf8'));
const normalize = (value) => {
  if (!value || typeof value !== 'object') return;

  // Generator 7.25.0 treats bare null as a non-nullable fictional Null model.
  // This equivalent schema still permits only null and preserves required keys.
  if (value.type === 'null') {
    value.type = ['object', 'null'];
    value.enum ??= [null];
  }

  for (const child of Object.values(value)) normalize(child);
};

normalize(contract);
await writeFile(output, `${JSON.stringify(contract)}\n`);
