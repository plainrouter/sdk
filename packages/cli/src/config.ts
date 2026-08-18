import { chmod, mkdir, readFile, rm, writeFile } from 'node:fs/promises';
import { homedir } from 'node:os';
import { dirname, join } from 'node:path';

export const DEFAULT_BASE_URL = 'https://plainrouter.com/api/v1';

export type StoredConfig = {
  token?: string;
  baseUrl?: string;
};

export type ResolvedConfig = {
  baseUrl: string;
  configPath: string;
  token?: string;
  tokenSource?: 'environment' | 'file';
};

const isRecord = (value: unknown): value is Record<string, unknown> =>
  typeof value === 'object' && value !== null && !Array.isArray(value);

export const getConfigPath = (
  environment: NodeJS.ProcessEnv = process.env,
  homeDirectory: string = homedir(),
): string => {
  const configHome = environment.XDG_CONFIG_HOME?.trim() ||
    join(homeDirectory, '.config');

  return join(configHome, 'plainrouter', 'config.json');
};

export const readStoredConfig = async (
  configPath: string,
): Promise<StoredConfig> => {
  let contents: string;

  try {
    contents = await readFile(configPath, 'utf8');
  } catch (error) {
    if ((error as NodeJS.ErrnoException).code === 'ENOENT') {
      return {};
    }

    throw error;
  }

  let parsed: unknown;

  try {
    parsed = JSON.parse(contents);
  } catch {
    throw new Error(`Config file is not valid JSON: ${configPath}`);
  }

  if (!isRecord(parsed)) {
    throw new Error(`Config file must contain a JSON object: ${configPath}`);
  }

  if (parsed.token !== undefined && typeof parsed.token !== 'string') {
    throw new Error(`Config token must be a string: ${configPath}`);
  }

  if (parsed.baseUrl !== undefined && typeof parsed.baseUrl !== 'string') {
    throw new Error(`Config baseUrl must be a string: ${configPath}`);
  }

  return {
    ...(typeof parsed.token === 'string' ? { token: parsed.token } : {}),
    ...(typeof parsed.baseUrl === 'string' ? { baseUrl: parsed.baseUrl } : {}),
  };
};

export const writeStoredConfig = async (
  configPath: string,
  config: StoredConfig,
): Promise<void> => {
  const configDirectory = dirname(configPath);

  await mkdir(configDirectory, { mode: 0o700, recursive: true });
  await chmod(configDirectory, 0o700);
  await writeFile(configPath, `${JSON.stringify(config, null, 2)}\n`, {
    mode: 0o600,
  });
  await chmod(configPath, 0o600);
};

export const saveToken = async (
  configPath: string,
  token: string,
): Promise<void> => {
  const existing = await readStoredConfig(configPath);

  await writeStoredConfig(configPath, {
    ...existing,
    token,
  });
};

export const removeStoredConfig = async (configPath: string): Promise<void> => {
  await rm(configPath, { force: true });
};

export const resolveConfig = async (
  environment: NodeJS.ProcessEnv = process.env,
  configPath: string = getConfigPath(environment),
): Promise<ResolvedConfig> => {
  const stored = await readStoredConfig(configPath);
  const environmentToken = environment.PLAINROUTER_TOKEN?.trim();
  const fileToken = stored.token?.trim();
  const token = environmentToken || fileToken;
  const environmentBaseUrl = environment.PLAINROUTER_BASE_URL?.trim();
  const fileBaseUrl = stored.baseUrl?.trim();

  return {
    baseUrl: environmentBaseUrl || fileBaseUrl || DEFAULT_BASE_URL,
    configPath,
    ...(token ? { token } : {}),
    ...(environmentToken
      ? { tokenSource: 'environment' as const }
      : fileToken
        ? { tokenSource: 'file' as const }
        : {}),
  };
};
