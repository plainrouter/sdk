import { describe, expect, it } from 'vitest';

import {
  zActionBatchRead,
  zActionPolicyRead,
  zActionReadItem,
  zCreateEventBody,
  zCreateEventResponse,
  zEvent,
  zGetEmqReportResponse,
  zVerifySignalIngestionResponse,
} from '../src/index.js';

describe('generated response schemas', () => {
  it('parses current policy responses and rejects an invalid execution mode', () => {
    const response = {
      data: {
        id: null,
        workspace_id: 1,
        execution_mode: 'full',
        outcome_check_after_hours: 24,
        anomaly_threshold_percent: '20.00',
      },
    };

    expect(zActionPolicyRead.parse(response)).toEqual(response);
    expect(() =>
      zActionPolicyRead.parse({
        data: { ...response.data, execution_mode: 'unknown_mode' },
      }),
    ).toThrow();
  });

  it('accepts halted Actions statuses and rejects an unknown status', () => {
    const disposition = {
      receipt_status: null,
      outcome_status: null,
      outcome_reason_code: null,
      outcome_checked_at: null,
      outcome_payload: null,
      compensation_reason_code: null,
      recovery_disposition: null,
      late_restored: false,
    };
    const policyResult = {
      id: 'policy-result-1',
      policy_id: 'policy-1',
      policy_version: 1,
      phase: 'execution',
      outcome: 'blocked',
      reasons: ['account_inactive'],
      reason_details: null,
      requested_minor: null,
      evaluated_at: '2026-10-10T10:00:00Z',
    };
    const action = {
      id: '01JTESTACTION0000000000000',
      batch_id: '01JTESTBATCH00000000000000',
      workspace_id: 1,
      type: 'pause',
      target_entity_type: 'ad',
      target_entity_id: '120000000000001',
      target_entity_name: null,
      params: {},
      rationale: 'Pause the ad while the batch is halted.',
      status: 'blocked',
      batch_status: 'halted',
      disposition,
      policy_result: policyResult,
      policy_results: [policyResult],
      policy_decision: null,
      policy_reasons: [],
    };
    const batch = {
      data: {
        id: '01JTESTBATCH00000000000000',
        workspace_id: 1,
        platform_ad_account_id: 1,
        status: 'halted',
        batch_status: 'halted',
        restoration_summary: null,
        policy_decision: null,
        policy_reasons: [],
        rationale: 'Pause the ad while the batch is halted.',
        idempotency_key: 'test-halted-batch',
        actions: [action],
      },
    };

    expect(zActionBatchRead.parse(batch)).toEqual(batch);
    expect(zActionReadItem.parse(action)).toEqual(action);
    expect(() =>
      zActionReadItem.parse({
        ...action,
        policy_result: { ...policyResult, phase: 'unknown_phase' },
      }),
    ).toThrow();
    expect(() =>
      zActionBatchRead.parse({
        data: { ...batch.data, status: 'unknown_status' },
      }),
    ).toThrow();
  });

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
      workspace_id: 1,
      consent: '{}',
      user_data_hashed: {},
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
