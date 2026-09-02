import { readFile } from 'node:fs/promises';

const expectedActor = 'bursteri';
const tag = process.env.GITHUB_REF_NAME ?? process.argv[2];
const actor = process.env.GITHUB_ACTOR;

if (!tag) {
  throw new Error('Release tag is required via GITHUB_REF_NAME or the first argument.');
}

const tagMatch = /^v(\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?)$/.exec(tag);

if (!tagMatch) {
  throw new Error(`Release tag ${tag} must use the v*.*.* format.`);
}

if (actor && actor !== expectedActor) {
  throw new Error(`Release tags must be pushed by ${expectedActor}, not ${actor}.`);
}

const releaseVersion = tagMatch[1];
const paths = {
  cli: new URL('../packages/cli/package.json', import.meta.url),
  sdk: new URL('../packages/sdk/package.json', import.meta.url),
  spec: new URL('../spec/openapi.json', import.meta.url),
};
const [cliPackage, sdkPackage, specification] = await Promise.all(
  Object.values(paths).map(async (path) => JSON.parse(await readFile(path, 'utf8'))),
);
const versions = {
  '@plainrouter/cli': cliPackage.version,
  '@plainrouter/sdk': sdkPackage.version,
};

for (const [source, version] of Object.entries(versions)) {
  if (version !== releaseVersion) {
    throw new Error(`${source} version ${String(version)} does not match tag ${tag}.`);
  }
}

if (specification['x-signed'] !== true) {
  throw new Error('The vendored OpenAPI contract is not signed.');
}

console.log(
  `Verified ${tag} for both npm packages targeting signed OpenAPI ${String(specification.info?.version)}.`,
);
