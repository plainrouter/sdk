import { describe, expect, it } from 'vitest';

import {
  zActionBatchRead,
  zActionPolicyRead,
  zActionProposalInput,
  zActionReadItem,
  zActionsApiProposeBody,
  zActionsRulesStoreBody,
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

  it('validates closed request objects and preserves open consent fields', () => {
    const request = {
      consent: { analytics_storage: 'granted' },
      consent_basis: 'consent',
      consent_mode: { ad_user_data: 'granted' },
      event_name: 'Purchase',
      tcf: { string: 'test-tcf-string' },
    };

    expect(zCreateEventBody.parse(request)).toEqual(request);
    expect(() => zCreateEventBody.parse({ event_name: 'Purchase' })).toThrow();

    const openObject = {
      ...request,
      consent: { analytics_storage: 'granted', custom_consent_flag: 'allowed' },
    };
    expect(zCreateEventBody.parse(openObject).consent).toEqual(openObject.consent);
    const proposal = {
      actions: [{
        type: 'increase_budget' as const,
        target_entity: { type: 'campaign' as const, id: '123' },
        params: { new_daily_budget_minor: 100 },
        rationale: 'Increase the campaign budget.',
      }, {
        type: 'pause' as const,
        target_entity: { type: 'ad' as const, id: '456' },
        params: {},
        rationale: 'Pause the ad.',
      }, {
        type: 'set_status' as const,
        target_entity: { type: 'ad' as const, id: '789' },
        params: { status: 'paused' as const },
        rationale: 'Pause the ad.',
      }],
      rationale: 'Apply the requested changes.',
      idempotency_key: 'closed-request-test',
      evidence: [{ source_tool: 'get_account_state' as const, fields_used: ['status'], action_index: 0 }],
      target_source: 'human_supplied' as const,
    };

    expect(zActionProposalInput.parse(proposal).actions).toEqual(proposal.actions);
    expect(zActionsApiProposeBody.parse(proposal).actions).toEqual(proposal.actions);

    const extraParams = {
      ...proposal,
      actions: [{
        ...proposal.actions[0]!,
        params: { ...proposal.actions[0]!.params, new_daily_budgets_minor: 100 },
      }],
    };
    const extraParamsResult = zActionProposalInput.safeParse(extraParams);
    expect(extraParamsResult.success).toBe(false);
    if (!extraParamsResult.success) {
      expect(extraParamsResult.error.issues[0]?.message).toContain('new_daily_budgets_minor');
      expect(extraParamsResult.error.issues[0]?.message).toContain('ActionProposalInput.actions[].params');
      const issue = extraParamsResult.error.issues[0];
      expect(issue?.code).toBe('invalid_union');
      if (issue?.code === 'invalid_union') {
        expect(issue.errors).toHaveLength(1);
        expect(issue.errors[0]?.[0]?.message).toContain('anyOf[0]');
      }
    }
    const budgetCaseVariantResult = zActionProposalInput.safeParse({
      ...proposal,
      actions: [{
        ...proposal.actions[0]!,
        params: {
          new_daily_budget_minor: 100,
          New_Daily_Budget_Minor: 100,
        },
      }],
    });
    expect(budgetCaseVariantResult.success).toBe(false);
    if (!budgetCaseVariantResult.success) {
      expect(budgetCaseVariantResult.error.issues[0]?.message).toContain('New_Daily_Budget_Minor');
      expect(budgetCaseVariantResult.error.issues[0]?.message).toContain('ActionProposalInput.actions[].params');
    }
    const extendedProposalSchema = zActionProposalInput.extend({});
    expect(extendedProposalSchema.shape.actions).toBeDefined();
    const extendedExtraParamsResult = extendedProposalSchema.safeParse(extraParams);
    expect(extendedExtraParamsResult.success).toBe(false);
    if (!extendedExtraParamsResult.success) {
      expect(extendedExtraParamsResult.error.issues[0]?.message).toContain('new_daily_budgets_minor');
      expect(extendedExtraParamsResult.error.issues[0]?.message).toContain('ActionProposalInput.actions[].params');
    }

    expect(zActionsApiProposeBody.shape.actions).toBeDefined();
    expect(zActionsApiProposeBody.extend({}).parse(proposal).actions).toEqual(proposal.actions);

    const extraEmptyParams = {
      ...proposal,
      actions: [{ ...proposal.actions[1]!, params: { unlisted_param: true } }],
    };
    const extraEmptyParamsResult = zActionProposalInput.safeParse(extraEmptyParams);
    expect(extraEmptyParamsResult.success).toBe(false);
    if (!extraEmptyParamsResult.success) {
      expect(extraEmptyParamsResult.error.issues[0]?.message).toContain('unlisted_param');
      expect(extraEmptyParamsResult.error.issues[0]?.message).toContain('ActionProposalInput.actions[].params');
    }

    const caseVariant = {
      ...proposal,
      actions: [{
        ...proposal.actions[2]!,
        params: { status: 'paused' as const, Status: 'paused' },
      }],
    };
    const caseVariantResult = zActionProposalInput.safeParse(caseVariant);
    expect(caseVariantResult.success).toBe(false);
    if (!caseVariantResult.success) {
      expect(caseVariantResult.error.issues[0]?.message).toContain('Status');
      expect(caseVariantResult.error.issues[0]?.message).toContain('ActionProposalInput.actions[].params');
    }

    const extraStatusParamResult = zActionProposalInput.safeParse({
      ...proposal,
      actions: [{
        ...proposal.actions[2]!,
        params: { status: 'paused' as const, statuz: 'paused' },
      }],
    });
    expect(extraStatusParamResult.success).toBe(false);
    if (!extraStatusParamResult.success) {
      expect(extraStatusParamResult.error.issues[0]?.message).toContain('statuz');
      expect(extraStatusParamResult.error.issues[0]?.message).toContain('ActionProposalInput.actions[].params');
    }

    const duplicateProposal = {
      ...proposal,
      actions: [{
        type: 'duplicate_ad_with_creative' as const,
        target_entity: { type: 'ad' as const, id: '789' },
        params: { asset_id: 'image:asset-456', status: 'paused' as const },
        rationale: 'Duplicate the ad with the supplied creative.',
      }],
    };
    expect(zActionProposalInput.safeParse(duplicateProposal).success).toBe(true);
    const extraDuplicateParamResult = zActionProposalInput.safeParse({
      ...duplicateProposal,
      actions: [{
        ...duplicateProposal.actions[0]!,
        params: { ...duplicateProposal.actions[0]!.params, asset_ids: 'image:asset-456' },
      }],
    });
    expect(extraDuplicateParamResult.success).toBe(false);
    if (!extraDuplicateParamResult.success) {
      expect(extraDuplicateParamResult.error.issues[0]?.message).toContain('asset_ids');
      expect(extraDuplicateParamResult.error.issues[0]?.message).toContain('ActionProposalInput.actions[].params');
    }
    const duplicateCaseVariantResult = zActionProposalInput.safeParse({
      ...duplicateProposal,
      actions: [{
        ...duplicateProposal.actions[0]!,
        params: { ...duplicateProposal.actions[0]!.params, Asset_ID: 'image:asset-456' },
      }],
    });
    expect(duplicateCaseVariantResult.success).toBe(false);
    if (!duplicateCaseVariantResult.success) {
      expect(duplicateCaseVariantResult.error.issues[0]?.message).toContain('Asset_ID');
      expect(duplicateCaseVariantResult.error.issues[0]?.message).toContain('ActionProposalInput.actions[].params');
    }

    const extraTarget = {
      ...proposal,
      actions: [{
        ...proposal.actions[0]!,
        target_entity: { ...proposal.actions[0]!.target_entity, CampaignID: '123' },
      }],
    };
    const extraTargetResult = zActionProposalInput.safeParse(extraTarget);
    expect(extraTargetResult.success).toBe(false);
    if (!extraTargetResult.success) {
      expect(extraTargetResult.error.issues[0]?.message).toContain('CampaignID');
      expect(extraTargetResult.error.issues[0]?.message).toContain('ActionProposalInput.actions[].target_entity');
    }

    const extraRuleDefinition = zActionsRulesStoreBody.safeParse({
      name: 'Pause expensive ads',
      platform_ad_account_id: 1,
      definition: {
        target_level: 'ad_set',
        action: 'pause',
        minimum_counted_arrivals: 50,
        cost_comparison: 'at_least',
        cost_ratio: 1,
        budget_change_percent: 5,
      },
    });
    expect(extraRuleDefinition.success).toBe(false);
    if (!extraRuleDefinition.success) {
      expect(extraRuleDefinition.error.issues[0]?.message).toContain('budget_change_percent');
      expect(extraRuleDefinition.error.issues[0]?.message).toContain('ActionsRulesStoreBody.definition');
    }

    const documentedRuleDefinition = zActionsRulesStoreBody.parse({
      name: 'Pause expensive ads',
      platform_ad_account_id: 1,
      definition: {
        target_level: 'ad_set',
        action: 'pause',
        minimum_counted_arrivals: 50,
        cost_comparison: 'at_least',
        cost_ratio: 1,
      },
    });
    expect(documentedRuleDefinition.definition).toEqual({
      target_level: 'ad_set',
      action: 'pause',
      minimum_counted_arrivals: 50,
      cost_comparison: 'at_least',
      cost_ratio: 1,
    });
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
