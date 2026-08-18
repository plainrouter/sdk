import { appendFile, readFile } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';

const [metadataPath, packageKind, environmentVariable] = process.argv.slice(2);

if (!metadataPath || !['sdk', 'cli'].includes(packageKind)) {
  throw new Error('Usage: node scripts/verify-pack.mjs <metadata.json> <sdk|cli> [env-name]');
}

const metadata = JSON.parse(await readFile(metadataPath, 'utf8'));

if (!Array.isArray(metadata) || metadata.length !== 1) {
  throw new Error('Expected npm pack to return metadata for exactly one package.');
}

const packageMetadata = metadata[0];
const files = packageMetadata.files.map(({ path }) => path).sort();
const requiredFiles = ['LICENSE', 'README.md', 'package.json'];

if (packageKind === 'cli') {
  requiredFiles.push('bin/plainrouter.js');
}

for (const requiredFile of requiredFiles) {
  if (!files.includes(requiredFile)) {
    throw new Error(`${packageMetadata.name} tarball is missing ${requiredFile}.`);
  }
}

const isAllowed = (path) =>
  requiredFiles.includes(path) ||
  (path.startsWith('dist/') && (path.endsWith('.js') || path.endsWith('.d.ts')));
const unexpectedFiles = files.filter((path) => !isAllowed(path));

if (unexpectedFiles.length > 0) {
  throw new Error(
    `${packageMetadata.name} tarball contains unexpected files: ${unexpectedFiles.join(', ')}`,
  );
}

if (!files.some((path) => path.startsWith('dist/') && path.endsWith('.js'))) {
  throw new Error(`${packageMetadata.name} tarball contains no built JavaScript.`);
}

if (!files.some((path) => path.startsWith('dist/') && path.endsWith('.d.ts'))) {
  throw new Error(`${packageMetadata.name} tarball contains no type declarations.`);
}

console.log(`${packageMetadata.name}@${packageMetadata.version} tarball verified:`);

for (const path of files) {
  console.log(`- ${path}`);
}

if (environmentVariable && process.env.GITHUB_ENV) {
  const tarballPath = resolve(dirname(metadataPath), packageMetadata.filename);

  await appendFile(process.env.GITHUB_ENV, `${environmentVariable}=${tarballPath}\n`);
}
