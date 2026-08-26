import { readFile } from 'node:fs/promises';

const readJson = async (path) => JSON.parse(await readFile(new URL(path, import.meta.url), 'utf8'));
const [workspace, sdk, cli, specification] = await Promise.all([
  readJson('../package.json'),
  readJson('../packages/sdk/package.json'),
  readJson('../packages/cli/package.json'),
  readJson('../spec/openapi.json'),
]);

const expectedVersion = specification.info?.version;

for (const [name, packageMetadata] of [
  ['workspace', workspace],
  ['@plainrouter/sdk', sdk],
  ['@plainrouter/cli', cli],
]) {
  if (packageMetadata.version !== expectedVersion) {
    throw new Error(`${name} version ${packageMetadata.version} does not match signed contract ${expectedVersion}.`);
  }

  if (packageMetadata.engines?.node !== '>=22.22.2') {
    throw new Error(`${name} must declare the verified Node range >=22.22.2.`);
  }
}

for (const [name, packageMetadata, directory] of [
  ['@plainrouter/sdk', sdk, 'packages/sdk'],
  ['@plainrouter/cli', cli, 'packages/cli'],
]) {
  if (packageMetadata.homepage !== 'https://plainrouter.com') {
    throw new Error(`${name} homepage must identify https://plainrouter.com.`);
  }

  if (packageMetadata.repository?.url !== 'git+https://github.com/wudaku/plainrouter-sdk.git') {
    throw new Error(`${name} repository URL is not the official SDK repository.`);
  }

  if (packageMetadata.repository?.directory !== directory) {
    throw new Error(`${name} repository directory must be ${directory}.`);
  }
}

if (cli.bin?.plainrouter !== './bin/plainrouter.js') {
  throw new Error('@plainrouter/cli must publish the plainrouter executable.');
}

console.log(`Verified official npm metadata for SDK and CLI ${expectedVersion}.`);
