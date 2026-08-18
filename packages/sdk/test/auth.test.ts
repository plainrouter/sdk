import { describe, expect, it, vi } from 'vitest';

import {
  configurePlainrouter,
  createEvent,
  getEmqReport,
  verifySignalIngestion,
} from '../src/index.js';

describe('signalTrackerSecret authentication', () => {
  it('sets the bearer header from injected configuration without a network call', async () => {
    const requests: Request[] = [];
    const fetchMock = vi.fn<typeof globalThis.fetch>(async (input, init) => {
      requests.push(
        input instanceof Request ? input : new Request(input, init),
      );

      return new Response(JSON.stringify({ snapshots: [] }), {
        headers: { 'Content-Type': 'application/json' },
        status: 200,
      });
    });

    configurePlainrouter({
      baseUrl: 'https://example.test/api/v1',
      fetch: fetchMock,
      signalTrackerSecret: 'tracker-test-secret',
    });

    const result = await getEmqReport();

    expect(result.data).toEqual({ snapshots: [] });
    expect(fetchMock).toHaveBeenCalledOnce();

    expect(requests).toHaveLength(1);
    expect(requests[0]?.headers.get('Authorization')).toBe(
      'Bearer tracker-test-secret',
    );
  });

  it('calls verification ingestion with bearer authentication', async () => {
    const requests: Request[] = [];
    const fetchMock = vi.fn<typeof globalThis.fetch>(async (input, init) => {
      requests.push(
        input instanceof Request ? input : new Request(input, init),
      );

      return new Response(
        JSON.stringify({ event_id: 'signal-verification', duplicate: false }),
        {
          headers: { 'Content-Type': 'application/json' },
          status: 202,
        },
      );
    });

    configurePlainrouter({
      baseUrl: 'https://example.test/api/v1',
      fetch: fetchMock,
      signalTrackerSecret: 'tracker-test-secret',
    });

    const result = await verifySignalIngestion();

    expect(result.data).toEqual({
      event_id: 'signal-verification',
      duplicate: false,
    });
    expect(requests[0]?.method).toBe('POST');
    expect(requests[0]?.url).toBe(
      'https://example.test/api/v1/verification-events',
    );
    expect(requests[0]?.headers.get('Authorization')).toBe(
      'Bearer tracker-test-secret',
    );
  });

  it('serializes consent fields on event requests', async () => {
    const requests: Request[] = [];
    const fetchMock = vi.fn<typeof globalThis.fetch>(async (input, init) => {
      requests.push(
        input instanceof Request ? input : new Request(input, init),
      );

      return new Response(
        JSON.stringify({ event_id: 'event-123', duplicate: false }),
        {
          headers: { 'Content-Type': 'application/json' },
          status: 202,
        },
      );
    });

    configurePlainrouter({
      baseUrl: 'https://example.test/api/v1',
      fetch: fetchMock,
      signalTrackerSecret: 'tracker-test-secret',
    });

    await createEvent({
      body: {
        consent: { analytics_storage: 'granted' },
        consent_basis: 'consent',
        consent_mode: { ad_user_data: 'granted' },
        event_name: 'Purchase',
        tcf: { string: 'test-tcf-string' },
      },
    });

    await expect(requests[0]?.json()).resolves.toEqual({
      consent: { analytics_storage: 'granted' },
      consent_basis: 'consent',
      consent_mode: { ad_user_data: 'granted' },
      event_name: 'Purchase',
      tcf: { string: 'test-tcf-string' },
    });
  });
});
