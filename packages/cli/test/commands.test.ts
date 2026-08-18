import { describe, expect, it, vi } from 'vitest';

import {
  runCli,
  type CliDependencies,
  type SdkOperations,
} from '../src/index.js';

const successfulOperation = () =>
  vi.fn(async (_options?: unknown) => ({
    data: { ok: true },
  }));

const createSdk = (): SdkOperations => ({
  configure: vi.fn(),
  createEvent: successfulOperation(),
  deleteUserData: successfulOperation(),
  getEmqReport: vi.fn(async () => ({ data: { snapshots: [] } })),
  getEvent: successfulOperation(),
  getReconciliationReport: successfulOperation(),
  listEvents: successfulOperation(),
  replayDeliveries: successfulOperation(),
  sendTestPurchase: successfulOperation(),
  setDestinationTestMode: successfulOperation(),
});

const createHarness = (
  overrides: Partial<CliDependencies> = {},
): {
  dependencies: CliDependencies;
  sdk: SdkOperations;
  stderr: string[];
  stdout: string[];
} => {
  const sdk = overrides.sdk ?? createSdk();
  const stderr: string[] = [];
  const stdout: string[] = [];
  const dependencies: CliDependencies = {
    confirm: vi.fn(async () => true),
    configPath: () => '/tmp/plainrouter-cli-test/config.json',
    promptToken: vi.fn(async () => 'fixture-token-1234'),
    removeConfig: vi.fn(async () => undefined),
    resolveConfig: vi.fn(async () => ({
      baseUrl: 'https://plainrouter.com/api/v1',
      configPath: '/tmp/plainrouter-cli-test/config.json',
      token: 'fixture-token-1234',
      tokenSource: 'environment' as const,
    })),
    saveToken: vi.fn(async () => undefined),
    sdk,
    writeErr: (text) => stderr.push(text),
    writeOut: (text) => stdout.push(text),
    ...overrides,
  };

  return { dependencies, sdk, stderr, stdout };
};

const run = async (
  dependencies: CliDependencies,
  ...args: string[]
): Promise<number> => runCli(['node', 'plainrouter', ...args], dependencies);

describe('SDK operation commands', () => {
  it('maps events create to createEvent', async () => {
    const { dependencies, sdk, stdout } = createHarness();

    const exitCode = await run(
      dependencies,
      'events',
      'create',
      '--data',
      '{"event_name":"Purchase","event_id":"evt_1"}',
      '--json',
    );

    expect(exitCode).toBe(0);
    expect(sdk.createEvent).toHaveBeenCalledWith({
      body: { event_id: 'evt_1', event_name: 'Purchase' },
    });
    expect(stdout.join('')).toBe('{\n  "ok": true\n}\n');
  });

  it('maps events get to getEvent', async () => {
    const { dependencies, sdk } = createHarness();

    expect(await run(dependencies, 'events', 'get', 'evt_1')).toBe(0);
    expect(sdk.getEvent).toHaveBeenCalledWith({ path: { event: 'evt_1' } });
  });

  it('maps events list to listEvents', async () => {
    const { dependencies, sdk } = createHarness();

    expect(
      await run(dependencies, 'events', 'list', '--per-page', '25'),
    ).toBe(0);
    expect(sdk.listEvents).toHaveBeenCalledWith({ query: { per_page: 25 } });
  });

  it('maps destinations test-mode to setDestinationTestMode', async () => {
    const { dependencies, sdk } = createHarness();

    expect(
      await run(
        dependencies,
        'destinations',
        'test-mode',
        'dest_1',
        '--on',
        '--test-event-code',
        'TEST42',
      ),
    ).toBe(0);
    expect(sdk.setDestinationTestMode).toHaveBeenCalledWith({
      body: { enabled: true, test_event_code: 'TEST42' },
      path: { destination: 'dest_1' },
    });
  });

  it('maps destinations test-purchase to sendTestPurchase', async () => {
    const { dependencies, sdk } = createHarness();

    expect(
      await run(
        dependencies,
        'destinations',
        'test-purchase',
        'dest_1',
        '--value',
        '25.00',
        '--currency',
        'USD',
        '--order-id',
        'order_1',
      ),
    ).toBe(0);
    expect(sdk.sendTestPurchase).toHaveBeenCalledWith({
      body: { currency: 'USD', order_id: 'order_1', value: '25.00' },
      path: { destination: 'dest_1' },
    });
  });

  it('maps deliveries replay to replayDeliveries', async () => {
    const { dependencies, sdk } = createHarness();

    expect(
      await run(
        dependencies,
        'deliveries',
        'replay',
        '--delivery-id',
        '7',
        '--delivery-id',
        '9',
        '--event-name',
        'Purchase',
        '--limit',
        '50',
      ),
    ).toBe(0);
    expect(sdk.replayDeliveries).toHaveBeenCalledWith({
      body: {
        delivery_ids: [7, 9],
        event_name: 'Purchase',
        limit: 50,
      },
    });
  });

  it('maps reports reconciliation to getReconciliationReport', async () => {
    const { dependencies, sdk } = createHarness();

    expect(
      await run(
        dependencies,
        'reports',
        'reconciliation',
        '--date',
        '2026-08-18',
      ),
    ).toBe(0);
    expect(sdk.getReconciliationReport).toHaveBeenCalledWith({
      query: { date: '2026-08-18' },
    });
  });

  it('maps reports emq to getEmqReport', async () => {
    const { dependencies, sdk } = createHarness();

    expect(await run(dependencies, 'reports', 'emq')).toBe(0);
    expect(sdk.getEmqReport).toHaveBeenCalledWith();
  });

  it('maps user-data delete to deleteUserData', async () => {
    const { dependencies, sdk } = createHarness();

    expect(
      await run(
        dependencies,
        'user-data',
        'delete',
        '--type',
        'email',
        '--hash',
        'hashed_identifier',
        '--yes',
      ),
    ).toBe(0);
    expect(sdk.deleteUserData).toHaveBeenCalledWith({
      body: {
        identifier_hash: 'hashed_identifier',
        identifier_type: 'email',
      },
    });
  });
});

describe('CLI safety and errors', () => {
  it('does not call deleteUserData when confirmation is declined', async () => {
    const { dependencies, sdk, stdout } = createHarness({
      confirm: vi.fn(async () => false),
    });

    expect(
      await run(
        dependencies,
        'user-data',
        'delete',
        '--type',
        'email',
        '--hash',
        'hashed_identifier',
      ),
    ).toBe(0);
    expect(sdk.deleteUserData).not.toHaveBeenCalled();
    expect(stdout.join('')).toContain('Deletion cancelled.');
  });

  it('writes shared validation errors to stderr with a nonzero exit', async () => {
    const sdk = createSdk();
    vi.mocked(sdk.createEvent).mockResolvedValueOnce({
      error: {
        errors: { event_name: ['The event name field is required.'] },
        message: 'The given data was invalid.',
      },
      response: new Response(null, { status: 422 }),
    });
    const { dependencies, stderr } = createHarness({ sdk });

    expect(
      await run(dependencies, 'events', 'create', '--data', '{}'),
    ).toBe(1);
    expect(stderr.join('')).toContain('API error (HTTP 422)');
    expect(stderr.join('')).toContain(
      'event_name: The event name field is required.',
    );
  });

  it('writes shared message errors to stderr with a nonzero exit', async () => {
    const sdk = createSdk();
    vi.mocked(sdk.getEmqReport).mockResolvedValueOnce({
      error: { message: 'Unauthenticated.' },
      response: new Response(null, { status: 401 }),
    });
    const { dependencies, stderr } = createHarness({ sdk });

    expect(await run(dependencies, 'reports', 'emq')).toBe(1);
    expect(stderr.join('')).toBe('API error (HTTP 401): Unauthenticated.\n');
  });
});

describe('authentication commands', () => {
  it('stores a pasted token without printing it', async () => {
    const { dependencies, stdout } = createHarness();

    expect(await run(dependencies, 'auth', 'login')).toBe(0);
    expect(dependencies.saveToken).toHaveBeenCalledWith(
      '/tmp/plainrouter-cli-test/config.json',
      'fixture-token-1234',
    );
    expect(stdout.join('')).not.toContain('fixture-token-1234');
  });

  it('removes the stored config on logout', async () => {
    const { dependencies } = createHarness();

    expect(await run(dependencies, 'auth', 'logout')).toBe(0);
    expect(dependencies.removeConfig).toHaveBeenCalledWith(
      '/tmp/plainrouter-cli-test/config.json',
    );
  });

  it('shows only the masked suffix and active source', async () => {
    const { dependencies, stdout } = createHarness();

    expect(await run(dependencies, 'auth', 'status', '--json')).toBe(0);
    expect(stdout.join('')).toContain('••••1234');
    expect(stdout.join('')).toContain('PLAINROUTER_TOKEN');
    expect(stdout.join('')).not.toContain('fixture-token-1234');
  });
});
