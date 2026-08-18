import { spawnSync } from 'node:child_process';

const helpCommands = [
  [],
  ['auth'],
  ['auth', 'login'],
  ['auth', 'logout'],
  ['auth', 'status'],
  ['events'],
  ['events', 'create'],
  ['events', 'get'],
  ['events', 'list'],
  ['destinations'],
  ['destinations', 'test-mode'],
  ['destinations', 'test-purchase'],
  ['deliveries'],
  ['deliveries', 'replay'],
  ['reports'],
  ['reports', 'reconciliation'],
  ['reports', 'emq'],
  ['user-data'],
  ['user-data', 'delete'],
];

const run = (args, environment = process.env) => {
  const result = spawnSync(
    process.execPath,
    ['packages/cli/bin/plainrouter.js', ...args],
    {
      env: environment,
      stdio: 'inherit',
    },
  );

  if (result.status !== 0) {
    process.exit(result.status ?? 1);
  }
};

for (const command of helpCommands) {
  run([...command, '--help']);
}

if (!process.env.PLAINROUTER_TOKEN) {
  console.error('PLAINROUTER_TOKEN must be set for the live events list smoke.');
  process.exit(1);
}

run(['events', 'list', '--json']);
