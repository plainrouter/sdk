import { mkdtemp, rm, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { spawnSync } from 'node:child_process';

const attempts = 5;
const retryDelayMilliseconds = 10_000;
const tag = process.env.GITHUB_REF_NAME;
const requestedVersion = process.argv[2] ?? (tag?.startsWith('v') ? tag.slice(1) : undefined);

if (!requestedVersion || !/^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$/.test(requestedVersion)) {
  throw new Error('Usage: node scripts/post-publish-smoke.mjs <version>');
}

const run = (command, args, cwd) =>
  spawnSync(command, args, {
    cwd,
    encoding: 'utf8',
    env: process.env,
    stdio: 'pipe',
  });
const wait = (milliseconds) => new Promise((resolve) => setTimeout(resolve, milliseconds));

let lastFailure;

for (let attempt = 1; attempt <= attempts; attempt += 1) {
  const installationDirectory = await mkdtemp(join(tmpdir(), 'plainrouter-release-smoke-'));

  try {
    await writeFile(
      join(installationDirectory, 'package.json'),
      `${JSON.stringify({ name: 'plainrouter-release-smoke', private: true, type: 'module' }, null, 2)}\n`,
    );

    const installation = run(
      'corepack',
      [
        'npm@11.19.0',
        'install',
        '--ignore-scripts',
        '--no-audit',
        '--no-fund',
        `@plainrouter/sdk@${requestedVersion}`,
        `@plainrouter/cli@${requestedVersion}`,
      ],
      installationDirectory,
    );

    if (installation.status !== 0) {
      throw new Error(installation.stderr.trim() || installation.stdout.trim());
    }

    const sdkImport = run(
      process.execPath,
      ['--input-type=module', '--eval', "await import('@plainrouter/sdk');"],
      installationDirectory,
    );

    if (sdkImport.status !== 0) {
      throw new Error(sdkImport.stderr.trim() || sdkImport.stdout.trim());
    }

    const cliHelp = run(
      join(installationDirectory, 'node_modules', '.bin', 'plainrouter'),
      ['--help'],
      installationDirectory,
    );

    if (cliHelp.status !== 0 || !cliHelp.stdout.includes('Plainrouter Signals API')) {
      throw new Error(cliHelp.stderr.trim() || cliHelp.stdout.trim() || 'CLI help output was unexpected.');
    }

    console.log(`Verified published @plainrouter/sdk and @plainrouter/cli ${requestedVersion}.`);
    lastFailure = undefined;
    break;
  } catch (error) {
    lastFailure = error;

    if (attempt < attempts) {
      console.warn(`Registry smoke attempt ${attempt} failed; retrying in 10 seconds.`);
      await wait(retryDelayMilliseconds);
    }
  } finally {
    await rm(installationDirectory, { recursive: true, force: true });
  }
}

if (lastFailure) {
  throw lastFailure;
}
