import {
  configurePlainrouter,
  createEvent,
  deleteUserData,
  getEmqReport,
  getEvent,
  getReconciliationReport,
  listEvents,
  replayDeliveries,
  sendTestPurchase,
  setDestinationTestMode,
  type CreateEventData,
  type DeleteUserDataData,
  type GetReconciliationReportData,
  type ReplayDeliveriesData,
  type SendTestPurchaseData,
} from '@plainrouter/sdk';
import {
  Command,
  CommanderError,
  InvalidArgumentError,
  Option,
} from 'commander';

import {
  getConfigPath,
  removeStoredConfig,
  resolveConfig,
  saveToken,
  type ResolvedConfig,
} from './config.js';
import {
  formatApiError,
  maskToken,
  writeResponse,
  type TextWriter,
} from './output.js';
import { confirmAction, promptForToken } from './prompt.js';

type ApiResult = {
  data?: unknown;
  error?: unknown;
  response?: Response;
};

export type SdkOperations = {
  configure: (config: { baseUrl: string; token: string }) => void;
  createEvent: (
    options: Parameters<typeof createEvent>[0],
  ) => Promise<ApiResult>;
  deleteUserData: (
    options: Parameters<typeof deleteUserData>[0],
  ) => Promise<ApiResult>;
  getEmqReport: () => Promise<ApiResult>;
  getEvent: (
    options: Parameters<typeof getEvent>[0],
  ) => Promise<ApiResult>;
  getReconciliationReport: (
    options: Parameters<typeof getReconciliationReport>[0],
  ) => Promise<ApiResult>;
  listEvents: (
    options?: Parameters<typeof listEvents>[0],
  ) => Promise<ApiResult>;
  replayDeliveries: (
    options?: Parameters<typeof replayDeliveries>[0],
  ) => Promise<ApiResult>;
  sendTestPurchase: (
    options: Parameters<typeof sendTestPurchase>[0],
  ) => Promise<ApiResult>;
  setDestinationTestMode: (
    options: Parameters<typeof setDestinationTestMode>[0],
  ) => Promise<ApiResult>;
};

export type CliDependencies = {
  confirm: (question: string) => Promise<boolean>;
  configPath: () => string;
  promptToken: (question: string) => Promise<string>;
  removeConfig: (configPath: string) => Promise<void>;
  resolveConfig: () => Promise<ResolvedConfig>;
  saveToken: (configPath: string, token: string) => Promise<void>;
  sdk: SdkOperations;
  writeErr: TextWriter;
  writeOut: TextWriter;
};

class CliError extends Error {}

class ApiError extends Error {
  public constructor(
    message: string,
    public readonly status?: number,
  ) {
    super(message);
  }
}

const defaultSdk: SdkOperations = {
  configure: ({ baseUrl, token }) => {
    configurePlainrouter({ baseUrl, signalTrackerSecret: token });
  },
  createEvent: (options) => createEvent(options),
  deleteUserData: (options) => deleteUserData(options),
  getEmqReport: () => getEmqReport(),
  getEvent: (options) => getEvent(options),
  getReconciliationReport: (options) =>
    getReconciliationReport(options),
  listEvents: (options) => listEvents(options),
  replayDeliveries: (options) => replayDeliveries(options),
  sendTestPurchase: (options) => sendTestPurchase(options),
  setDestinationTestMode: (options) =>
    setDestinationTestMode(options),
};

export const createDefaultDependencies = (): CliDependencies => {
  const configPath = (): string => getConfigPath();

  return {
    confirm: (question) => confirmAction(question),
    configPath,
    promptToken: (question) => promptForToken(question),
    removeConfig: removeStoredConfig,
    resolveConfig: () => resolveConfig(process.env, configPath()),
    saveToken,
    sdk: defaultSdk,
    writeErr: (text) => process.stderr.write(text),
    writeOut: (text) => process.stdout.write(text),
  };
};

const parseJsonObject = (value: string): Record<string, unknown> => {
  let parsed: unknown;

  try {
    parsed = JSON.parse(value);
  } catch {
    throw new InvalidArgumentError('must be a valid JSON object');
  }

  if (typeof parsed !== 'object' || parsed === null || Array.isArray(parsed)) {
    throw new InvalidArgumentError('must be a JSON object');
  }

  return parsed as Record<string, unknown>;
};

const parseInteger = (value: string): number => {
  const parsed = Number(value);

  if (!Number.isInteger(parsed)) {
    throw new InvalidArgumentError('must be an integer');
  }

  return parsed;
};

const collectInteger = (value: string, previous: number[] = []): number[] => [
  ...previous,
  parseInteger(value),
];

const globalJson = (command: Command): boolean =>
  Boolean(command.optsWithGlobals().json);

const requireApiConfig = async (
  dependencies: CliDependencies,
): Promise<ResolvedConfig & { token: string }> => {
  const config = await dependencies.resolveConfig();

  if (!config.token) {
    throw new CliError(
      'No token configured. Set PLAINROUTER_TOKEN or run `plainrouter auth login`.',
    );
  }

  dependencies.sdk.configure({
    baseUrl: config.baseUrl,
    token: config.token,
  });

  return { ...config, token: config.token };
};

const executeApi = async (
  dependencies: CliDependencies,
  command: Command,
  call: () => Promise<ApiResult>,
): Promise<void> => {
  await requireApiConfig(dependencies);

  const result = await call();

  if (result.error !== undefined) {
    throw new ApiError(
      formatApiError(result.error),
      result.response?.status,
    );
  }

  if (result.data === undefined) {
    throw new ApiError('API response did not contain data.');
  }

  writeResponse(result.data, globalJson(command), dependencies.writeOut);
};

export const createProgram = (dependencies: CliDependencies): Command => {
  const program = new Command()
    .name('plainrouter')
    .description('Plainrouter Signals API command line interface')
    .version('0.5.0')
    .option('--json', 'emit the API response as JSON')
    .configureHelp({ showGlobalOptions: true })
    .configureOutput({
      writeErr: dependencies.writeErr,
      writeOut: dependencies.writeOut,
    })
    .exitOverride();

  const auth = program.command('auth').description('manage tracker authentication');

  auth
    .command('login')
    .description('paste and store a tracker token')
    .action(async (_options, command: Command) => {
      const token = await dependencies.promptToken('Paste tracker token: ');

      if (!token) {
        throw new CliError('Token cannot be empty.');
      }

      const configPath = dependencies.configPath();

      await dependencies.saveToken(configPath, token);
      writeResponse(
        { saved: true, path: configPath },
        globalJson(command),
        dependencies.writeOut,
      );
    });

  auth
    .command('logout')
    .description('remove the stored tracker token')
    .action(async (_options, command: Command) => {
      const configPath = dependencies.configPath();

      await dependencies.removeConfig(configPath);
      writeResponse(
        { removed: true, path: configPath },
        globalJson(command),
        dependencies.writeOut,
      );
    });

  auth
    .command('status')
    .description('show the active masked credential source')
    .action(async (_options, command: Command) => {
      const config = await dependencies.resolveConfig();
      const status = config.token
        ? {
            authenticated: true,
            token: maskToken(config.token),
            source: config.tokenSource === 'environment'
              ? 'PLAINROUTER_TOKEN'
              : config.configPath,
            base_url: config.baseUrl,
          }
        : {
            authenticated: false,
            source: 'none',
            base_url: config.baseUrl,
          };

      writeResponse(status, globalJson(command), dependencies.writeOut);
    });

  const events = program.command('events').description('create and inspect events');

  events
    .command('create')
    .description('submit a Signal event')
    .requiredOption('--data <json>', 'event request body as a JSON object', parseJsonObject)
    .action(async (options: { data: Record<string, unknown> }, command: Command) => {
      await executeApi(dependencies, command, () =>
        dependencies.sdk.createEvent({
          body: options.data as CreateEventData['body'],
        }),
      );
    });

  events
    .command('get <id>')
    .description('get an event and its delivery state')
    .action(async (id: string, _options, command: Command) => {
      await executeApi(dependencies, command, () =>
        dependencies.sdk.getEvent({ path: { event: id } }),
      );
    });

  events
    .command('list')
    .description('list recent events and acceptance metrics')
    .option('--per-page <count>', 'events per page', parseInteger)
    .action(async (options: { perPage?: number }, command: Command) => {
      await executeApi(dependencies, command, () =>
        options.perPage === undefined
          ? dependencies.sdk.listEvents()
          : dependencies.sdk.listEvents({ query: { per_page: options.perPage } }),
      );
    });

  const destinations = program
    .command('destinations')
    .description('manage destination test operations');

  destinations
    .command('test-mode <id>')
    .description('enable or disable destination test mode')
    .addOption(new Option('--on', 'enable test mode').conflicts('off'))
    .addOption(new Option('--off', 'disable test mode').conflicts('on'))
    .option('--test-event-code <code>', 'optional platform test event code')
    .action(async (
      id: string,
      options: { off?: boolean; on?: boolean; testEventCode?: string },
      command: Command,
    ) => {
      if (!options.on && !options.off) {
        throw new CliError('Choose exactly one of --on or --off.');
      }

      await executeApi(dependencies, command, () =>
        dependencies.sdk.setDestinationTestMode({
          body: {
            enabled: Boolean(options.on),
            ...(options.testEventCode === undefined
              ? {}
              : { test_event_code: options.testEventCode }),
          },
          path: { destination: id },
        }),
      );
    });

  destinations
    .command('test-purchase <id>')
    .description('send a destination test purchase')
    .option('--value <amount>', 'purchase value')
    .option('--currency <code>', 'purchase currency')
    .option('--order-id <id>', 'purchase order ID')
    .action(async (
      id: string,
      options: { currency?: string; orderId?: string; value?: string },
      command: Command,
    ) => {
      const body: NonNullable<SendTestPurchaseData['body']> = {
        ...(options.value === undefined ? {} : { value: options.value }),
        ...(options.currency === undefined ? {} : { currency: options.currency }),
        ...(options.orderId === undefined ? {} : { order_id: options.orderId }),
      };

      await executeApi(dependencies, command, () =>
        dependencies.sdk.sendTestPurchase({
          ...(Object.keys(body).length === 0 ? {} : { body }),
          path: { destination: id },
        }),
      );
    });

  const deliveries = program
    .command('deliveries')
    .description('manage event deliveries');

  deliveries
    .command('replay')
    .description('queue eligible deliveries for replay')
    .option(
      '--delivery-id <id>',
      'delivery ID to replay; repeat for multiple IDs',
      collectInteger,
    )
    .option('--event-name <name>', 'limit replay to an event name')
    .option('--limit <count>', 'maximum deliveries to evaluate', parseInteger)
    .action(async (
      options: { deliveryId?: number[]; eventName?: string; limit?: number },
      command: Command,
    ) => {
      const body: NonNullable<ReplayDeliveriesData['body']> = {
        ...(!options.deliveryId || options.deliveryId.length === 0
          ? {}
          : { delivery_ids: options.deliveryId }),
        ...(options.eventName === undefined
          ? {}
          : { event_name: options.eventName }),
        ...(options.limit === undefined ? {} : { limit: options.limit }),
      };

      await executeApi(dependencies, command, () =>
        Object.keys(body).length === 0
          ? dependencies.sdk.replayDeliveries()
          : dependencies.sdk.replayDeliveries({ body }),
      );
    });

  const reports = program.command('reports').description('view Signal reports');

  reports
    .command('reconciliation')
    .description('get reconciliation reports for a date')
    .requiredOption('--date <date>', 'report date in YYYY-MM-DD format')
    .action(async (options: { date: string }, command: Command) => {
      await executeApi(dependencies, command, () =>
        dependencies.sdk.getReconciliationReport({
          query: { date: options.date } as GetReconciliationReportData['query'],
        }),
      );
    });

  reports
    .command('emq')
    .description('get event match quality snapshots')
    .action(async (_options, command: Command) => {
      await executeApi(dependencies, command, () =>
        dependencies.sdk.getEmqReport(),
      );
    });

  const userData = program
    .command('user-data')
    .description('manage data subject deletion');

  userData
    .command('delete')
    .description('delete matching user data')
    .requiredOption('--type <type>', 'identifier type: email, phone, or external_id')
    .requiredOption('--hash <hash>', 'hashed identifier value')
    .option('--yes', 'skip the confirmation prompt')
    .action(async (
      options: { hash: string; type: string; yes?: boolean },
      command: Command,
    ) => {
      if (!options.yes) {
        const confirmed = await dependencies.confirm(
          `Delete user data for identifier type ${options.type}?`,
        );

        if (!confirmed) {
          dependencies.writeOut('Deletion cancelled.\n');
          return;
        }
      }

      await executeApi(dependencies, command, () =>
        dependencies.sdk.deleteUserData({
          body: {
            identifier_hash: options.hash,
            identifier_type: options.type,
          } as DeleteUserDataData['body'],
        }),
      );
    });

  return program;
};

export const runCli = async (
  argv: readonly string[] = process.argv,
  dependencies: CliDependencies = createDefaultDependencies(),
): Promise<number> => {
  try {
    await createProgram(dependencies).parseAsync([...argv]);

    return 0;
  } catch (error) {
    if (error instanceof CommanderError) {
      return error.exitCode;
    }

    if (error instanceof ApiError) {
      const status = error.status === undefined ? '' : ` (HTTP ${error.status})`;

      dependencies.writeErr(`API error${status}: ${error.message}\n`);

      return 1;
    }

    const message = error instanceof Error ? error.message : String(error);

    dependencies.writeErr(`Error: ${message}\n`);

    return 1;
  }
};
