import { describe, expect, it } from 'vitest';

import {
  zCreateEventBody,
  zCreateEventResponse,
  zEvent,
  zGetEmqReportResponse,
  zVerifySignalIngestionResponse,
} from '../src/index.js';

describe('generated response schemas', () => {
  it('round-trips a valid POST /events response and rejects a broken response', () => {
    const response = {
      event_id: '01JTESTEVENT00000000000000',
      duplicate: false,
    };

    expect(
      zCreateEventResponse.parse(JSON.parse(JSON.stringify(response))),
    ).toEqual(response);
    expect(() =>
      zCreateEventResponse.parse({ event_id: 123, duplicate: false }),
    ).toThrow();
  });

  it('requires consent_basis and accepts the consent request fields', () => {
    const request = {
      consent: { analytics_storage: 'granted' },
      consent_basis: 'consent',
      consent_mode: { ad_user_data: 'granted' },
      event_name: 'Purchase',
      tcf: { string: 'test-tcf-string' },
    };

    expect(zCreateEventBody.parse(request)).toEqual(request);
    expect(() => zCreateEventBody.parse({ event_name: 'Purchase' })).toThrow();
  });

  it('parses verification responses', () => {
    const response = { event_id: 'signal-verification', duplicate: false };

    expect(zVerifySignalIngestionResponse.parse(response)).toEqual(response);
  });

  it('deserializes the new event decision fields', () => {
    const event = {
      id: 'event-123',
      signal_tracker_id: 'tracker-123',
      parent_event_id: null,
      event_name: 'Purchase',
      event_time: '2026-08-19T00:00:00Z',
      action_source: 'website',
      event_class: 'conversion',
      order_id: 'order-123',
      value_amount: 1995,
      value_currency: 'EUR',
      created_at: '2026-08-19T00:00:01Z',
      consent_basis: 'consent',
      measurement_class: 'advertising',
      attribution_join: 'allowed',
      enforcement_scope: 'event',
      policy_class: 'global',
      traffic_class: 'valid',
      consent_normalization_version: '1',
      consent: '{}',
      user_data_hashed: '{}',
      click_ids: '{}',
      session: '{}',
      value_data: '{}',
      event_source: 'https://example.test/checkout',
      payload_expired: false,
      deliveries: [],
    };

    expect(zEvent.parse(event)).toEqual(event);
  });

  it('round-trips a valid GET /reports/emq response and rejects a broken response', () => {
    const response = { snapshots: [] };

    expect(
      zGetEmqReportResponse.parse(JSON.parse(JSON.stringify(response))),
    ).toEqual(response);
    expect(() =>
      zGetEmqReportResponse.parse({ snapshots: 'not-an-array' }),
    ).toThrow();
  });
});
