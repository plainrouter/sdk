import { mkdtemp, rm, stat } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

import { afterEach, describe, expect, it } from 'vitest';

import {
  DEFAULT_BASE_URL,
  getConfigPath,
  resolveConfig,
  writeStoredConfig,
} from '../src/index.js';

const temporaryDirectories: string[] = [];

const createTemporaryDirectory = async (): Promise<string> => {
  const directory = await mkdtemp(join(tmpdir(), 'plainrouter-cli-config-'));

  temporaryDirectories.push(directory);

  return directory;
};

afterEach(async () => {
  await Promise.all(
    temporaryDirectories.splice(0).map((directory) =>
      rm(directory, { force: true, recursive: true }),
    ),
  );
});

describe('CLI authentication config', () => {
  it('uses XDG_CONFIG_HOME when it is set', () => {
    expect(
      getConfigPath({ XDG_CONFIG_HOME: '/xdg-config' }, '/home/example'),
    ).toBe('/xdg-config/plainrouter/config.json');
  });

  it('falls back to the home .config directory', () => {
    expect(getConfigPath({}, '/home/example')).toBe(
      '/home/example/.config/plainrouter/config.json',
    );
  });

  it('uses the stored token when the environment token is absent', async () => {
    const directory = await createTemporaryDirectory();
    const configPath = join(directory, 'plainrouter', 'config.json');

    await writeStoredConfig(configPath, { token: 'file-fixture-token' });

    await expect(resolveConfig({}, configPath)).resolves.toEqual({
      baseUrl: DEFAULT_BASE_URL,
      configPath,
      token: 'file-fixture-token',
      tokenSource: 'file',
    });
  });

  it('gives environment token and base URL precedence over the file', async () => {
    const directory = await createTemporaryDirectory();
    const configPath = join(directory, 'plainrouter', 'config.json');

    await writeStoredConfig(configPath, {
      baseUrl: 'https://file.example.test/api/v1',
      token: 'file-fixture-token',
    });

    await expect(
      resolveConfig(
        {
          PLAINROUTER_BASE_URL: 'https://environment.example.test/api/v1',
          PLAINROUTER_TOKEN: 'environment-fixture-token',
        },
        configPath,
      ),
    ).resolves.toEqual({
      baseUrl: 'https://environment.example.test/api/v1',
      configPath,
      token: 'environment-fixture-token',
      tokenSource: 'environment',
    });
  });

  it('writes the config file with owner-only permissions', async () => {
    const directory = await createTemporaryDirectory();
    const configPath = join(directory, 'plainrouter', 'config.json');

    await writeStoredConfig(configPath, { token: 'permission-fixture-token' });

    const configStat = await stat(configPath);

    expect(configStat.mode & 0o777).toBe(0o600);
  });
});
