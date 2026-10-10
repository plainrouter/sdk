import { describe, expect, it, vi } from 'vitest';

import {
  configurePlainrouter,
  createEvent,
  validateCreateEventBody,
  type CreateEventData,
  type IngestionWarningCode,
} from '../src/index.js';

const VALID_CAPTURED_AT = '2026-08-19T12:34:56.123456+02:00';
const VALID_CAPTURED_AT_Z = '2026-08-19T10:34:56Z';

type EventBody = CreateEventData['body'];

const eventBody = (overrides: Record<string, unknown> = {}): EventBody =>
  ({
    event_name: 'Purchase',
    consent_basis: 'consent',
    ...overrides,
  }) as EventBody;

const responseBody = {
  event_id: 'event-123',
  duplicate: false,
  warnings: [],
};

const configureWithResponse = (
  response: unknown = responseBody,
  status = 202,
): ReturnType<typeof vi.fn<typeof globalThis.fetch>> => {
  const fetchMock = vi.fn<typeof globalThis.fetch>(
    async (input, init) =>
      new Response(JSON.stringify(response), {
        headers: { 'Content-Type': 'application/json' },
        status,
      }),
  );

  configurePlainrouter({
    baseUrl: 'https://example.test/api/v1',
    fetch: fetchMock,
    signalTrackerSecret: 'tracker-test-secret',
  });

  return fetchMock;
};

const callCreateEvent = (body: EventBody) =>
  Promise.resolve().then(() => createEvent({ body }));

describe('consent.captured_at client validation', () => {
  it('rejects a visitor_id without captured_at before making an HTTP call', async () => {
    const fetchMock = configureWithResponse();

    await expect(
      callCreateEvent(eventBody({ visitor_id: 'visitor-123' })),
    ).rejects.toThrow(/consent\.captured_at.*(required|missing)/i);
    expect(fetchMock).not.toHaveBeenCalled();
  });

  it('rejects a user_data captured_at with a space separator before making a call', async () => {
    const fetchMock = configureWithResponse();

    await expect(
      callCreateEvent(
        eventBody({
          user_data: { em: 'hashed-email' },
          consent: { captured_at: '2026-08-19 12:34:56+02:00' },
        }),
      ),
    ).rejects.toThrow(/consent\.captured_at.*(invalid|format|ISO)/i);
    expect(fetchMock).not.toHaveBeenCalled();
  });

  it('sends a visitor_id with a valid captured_at byte-identical to the input', async () => {
    const fetchMock = configureWithResponse();
    const body = eventBody({
      visitor_id: 'visitor-123',
      consent: { captured_at: VALID_CAPTURED_AT },
    });

    await expect(callCreateEvent(body)).resolves.toMatchObject({
      data: { event_id: 'event-123', duplicate: false, warnings: [] },
    });

    expect(fetchMock).toHaveBeenCalledOnce();
    const request = fetchMock.mock.calls[0]?.[0];
    const requestInit = fetchMock.mock.calls[0]?.[1];
    if (request === undefined) {
      throw new Error('Expected the captured request input to be defined');
    }
    const requestObject =
      request instanceof Request
        ? request
        : new Request(request, requestInit);
    const rawBody = await requestObject.text();

    expect(rawBody).toContain(`"captured_at":"${VALID_CAPTURED_AT}"`);
    expect(JSON.parse(rawBody)).toMatchObject({
      visitor_id: 'visitor-123',
      consent: { captured_at: VALID_CAPTURED_AT },
    });
  });

  it('sends an event without visitor_id or user_data when captured_at is absent', async () => {
    const fetchMock = configureWithResponse();

    await expect(callCreateEvent(eventBody())).resolves.toMatchObject({
      data: { event_id: 'event-123', duplicate: false, warnings: [] },
    });
    expect(fetchMock).toHaveBeenCalledOnce();
  });

  it('treats explicit null visitor_id and user_data as absent', async () => {
    const fetchMock = configureWithResponse();
    const body = eventBody({
      visitor_id: null,
      user_data: null,
    });

    await expect(callCreateEvent(body)).resolves.toMatchObject({
      data: { event_id: 'event-123', duplicate: false, warnings: [] },
    });
    expect(fetchMock).toHaveBeenCalledOnce();
  });
});

describe('POST /events response warnings', () => {
  it.each([
    {
      code: 'consent_captured_at_invalid',
      field: 'consent.captured_at',
      message: 'Consent capture time must be ISO-8601.',
    },
    {
      code: 'event_source_invalid',
      field: 'event_source',
      message: 'Event source must be a valid URL.',
    },
  ] as const)('returns a typed 202 $code warning without throwing', async (warning) => {
    configureWithResponse(
      {
        event_id: 'event-warning',
        duplicate: false,
        warnings: [warning],
      },
      202,
    );

    const result = await createEvent({ body: eventBody() });

    expect(result.error).toBeUndefined();
    expect(result.data).toMatchObject({
      event_id: 'event-warning',
      duplicate: false,
      warnings: [warning],
    });

    if (!result.data || !('warnings' in result.data)) {
      throw new Error('Expected a typed 202 warning array');
    }

    const firstWarning = result.data.warnings[0];
    expect(firstWarning).toBeDefined();
    if (!firstWarning) {
      return;
    }

    const closedWarningCode: IngestionWarningCode = firstWarning.code;
    expect(closedWarningCode).toBe(warning.code);
    expect(firstWarning.field).toBe(warning.field);
    expect(firstWarning.message).toBe(warning.message);
  });

  it('returns a 200 duplicate without a warnings field and without throwing', async () => {
    configureWithResponse(
      { event_id: 'event-duplicate', duplicate: true },
      200,
    );

    const result = await createEvent({ body: eventBody() });

    expect(result.error).toBeUndefined();
    expect(result.data).toEqual({
      event_id: 'event-duplicate',
      duplicate: true,
    });
    expect(result.data && 'warnings' in result.data).toBe(false);
  });
});

describe('server captured_at fixture parity', () => {
  it.each([
    ['T with numeric offset', VALID_CAPTURED_AT, true],
    ['T with Z offset', VALID_CAPTURED_AT_Z, true],
    ['space separator', '2026-08-19 12:34:56+02:00', false],
    ['missing offset', '2026-08-19T12:34:56', false],
    ['empty', '', false],
    ['null', null, false],
  ])('%s has the server-compatible validation outcome', (_label, capturedAt, valid) => {
    const body = eventBody({
      visitor_id: 'visitor-123',
      consent: { captured_at: capturedAt },
    });

    if (valid) {
      expect(() => validateCreateEventBody(body)).not.toThrow();
    } else {
      expect(() => validateCreateEventBody(body)).toThrow(/consent\.captured_at/i);
    }
  });
});
