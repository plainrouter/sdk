import { describe, expect, it, vi } from 'vitest';

import {
  validateCreateEventBody,
  type CreateEventData,
} from '@plainrouter/sdk';

import {
  runCli,
  type CliDependencies,
  type SdkOperations,
} from '../src/index.js';

const VALID_CAPTURED_AT = '2026-08-19T12:34:56.123456+02:00';

type EventBody = Record<string, unknown>;

const successfulOperation = () =>
  vi.fn(async (_options?: unknown) => ({
    data: { event_id: 'event-123', duplicate: false, warnings: [] },
  }));

const createSdk = (): SdkOperations => ({
  configure: vi.fn(),
  createEvent: successfulOperation(),
  deleteUserData: successfulOperation(),
  getEmqReport: successfulOperation(),
  getEvent: successfulOperation(),
  getReconciliationReport: successfulOperation(),
  listEvents: successfulOperation(),
  replayDeliveries: successfulOperation(),
  sendTestPurchase: successfulOperation(),
  setDestinationTestMode: successfulOperation(),
});

const createHarness = (): {
  dependencies: CliDependencies;
  sdk: SdkOperations;
  stderr: string[];
  stdout: string[];
} => {
  const sdk = createSdk();
  const stderr: string[] = [];
  const stdout: string[] = [];
  const dependencies: CliDependencies = {
    confirm: vi.fn(async () => true),
    configPath: () => '/tmp/plainrouter-cli-captured-at/config.json',
    promptToken: vi.fn(async () => 'fixture-token-1234'),
    removeConfig: vi.fn(async () => undefined),
    resolveConfig: vi.fn(async () => ({
      baseUrl: 'https://example.test/api/v1',
      configPath: '/tmp/plainrouter-cli-captured-at/config.json',
      token: 'fixture-token-1234',
      tokenSource: 'environment' as const,
    })),
    saveToken: vi.fn(async () => undefined),
    sdk,
    writeErr: (text) => stderr.push(text),
    writeOut: (text) => stdout.push(text),
  };

  return { dependencies, sdk, stderr, stdout };
};

const run = async (
  dependencies: CliDependencies,
  body: EventBody,
): Promise<number> =>
  runCli([
    'node',
    'plainrouter',
    'events',
    'create',
    '--data',
    JSON.stringify(body),
  ], dependencies);

const validatorMessage = (body: EventBody): string => {
  try {
    validateCreateEventBody(body as CreateEventData['body']);
  } catch (error) {
    return error instanceof Error ? error.message : String(error);
  }

  throw new Error('Expected the fixture to fail SDK validation');
};

describe('TypeScript CLI consent.captured_at validation', () => {
  it.each([
    [
      'visitor_id without captured_at',
      {
        event_name: 'Purchase',
        consent_basis: 'consent',
        visitor_id: 'visitor-123',
      },
    ],
    [
      'user_data with a space separator',
      {
        event_name: 'Purchase',
        consent_basis: 'consent',
        user_data: { em: 'hashed-email' },
        consent: { captured_at: '2026-08-19 12:34:56+02:00' },
      },
    ],
  ])('%s exits nonzero with the shared validation message and makes no call', async (_label, body) => {
    const { dependencies, sdk, stderr } = createHarness();
    const expectedMessage = validatorMessage(body);

    expect(await run(dependencies, body)).toBe(1);
    expect(stderr.join('')).toContain(expectedMessage);
    expect(sdk.createEvent).not.toHaveBeenCalled();
    expect(sdk.configure).not.toHaveBeenCalled();
  });

  it('sends a valid captured_at input through the SDK operation', async () => {
    const { dependencies, sdk } = createHarness();
    const body = {
      event_name: 'Purchase',
      consent_basis: 'consent',
      visitor_id: 'visitor-123',
      consent: { captured_at: VALID_CAPTURED_AT },
    };

    expect(await run(dependencies, body)).toBe(0);
    expect(sdk.createEvent).toHaveBeenCalledOnce();
    expect(sdk.createEvent).toHaveBeenCalledWith({ body });
  });

  it('prints a 202 ingestion warning to stderr without failing the command', async () => {
    const { dependencies, sdk, stderr } = createHarness();
    const warning = {
      code: 'consent_captured_at_invalid',
      field: 'consent.captured_at',
      message: 'Consent capture time must be ISO-8601.',
    };
    vi.mocked(sdk.createEvent).mockResolvedValueOnce({
      data: {
        event_id: 'event-warning',
        duplicate: false,
        warnings: [warning],
      },
      response: new Response(null, { status: 202 }),
    });

    expect(
      await run(dependencies, {
        event_name: 'Purchase',
        consent_basis: 'consent',
      }),
    ).toBe(0);
    expect(stderr.join('')).toBe(
      'Warning: consent_captured_at_invalid (consent.captured_at): Consent capture time must be ISO-8601.\n',
    );
  });
});
