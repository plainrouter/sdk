import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';

const contractPath = new URL('../spec/openapi.json', import.meta.url);
const checksumPath = new URL('../spec/CHECKSUM', import.meta.url);

const [contractBytes, checksumText] = await Promise.all([
  readFile(contractPath),
  readFile(checksumPath, 'utf8'),
]);

const checksum = Object.fromEntries(
  checksumText
    .trim()
    .split('\n')
    .map((line) => {
      const separator = line.indexOf(':');

      return [line.slice(0, separator), line.slice(separator + 1).trim()];
    }),
);
const digest = createHash('sha256').update(contractBytes).digest('hex');
const contract = JSON.parse(contractBytes.toString('utf8'));

if (digest !== checksum.sha256) {
  throw new Error(`Vendored contract hash ${digest} does not match spec/CHECKSUM.`);
}

if (contract.info?.version !== checksum['info.version']) {
  throw new Error('Vendored contract version does not match spec/CHECKSUM.');
}

if (contract['x-signed'] !== true) {
  throw new Error('Vendored contract is not signed.');
}

if (checksum.source !== 'https://plainrouter.com/openapi.json') {
  throw new Error('Unexpected contract source URL.');
}

console.log(`Verified signed OpenAPI ${contract.info.version} (${digest}).`);
