import { describe, expect, expectTypeOf, it, vi } from 'vitest';
import {
  actionsApiDryRun as generatedActionsApiDryRun,
  actionsApiPropose as generatedActionsApiPropose,
} from '../src/generated/sdk.gen.js';

import {
  actionsApiDryRun,
  actionsApiPropose,
  configurePlainrouter,
  isRetryableProposalError,
  launchPlansExecute,
  launchPlansCopy,
  type ProposalUnavailable,
  type ActionProposalInput,
  zProposalUnavailable,
} from '../src/index.js';

if (false) {
  type ActionType = ActionProposalInput['actions'][number]['type'];
  type ParamsFor<T extends ActionType> = Extract<
    ActionProposalInput['actions'][number],
    { type: T }
  >['params'];
  const extraIncreaseBudget: ParamsFor<'increase_budget'> = {
    new_daily_budget_minor: 100,
    // @ts-expect-error Action params are closed by the OpenAPI contract.
    unlisted_param: true,
  };
  const extraDecreaseBudget: ParamsFor<'decrease_budget'> = {
    new_daily_budget_minor: 100,
    // @ts-expect-error Action params are closed by the OpenAPI contract.
    unlisted_param: true,
  };
  const extraPause: ParamsFor<'pause'> = {
    // @ts-expect-error Empty action params are closed by the OpenAPI contract.
    unlisted_param: true,
  };
  const extraResume: ParamsFor<'resume'> = {
    // @ts-expect-error Empty action params are closed by the OpenAPI contract.
    unlisted_param: true,
  };
  const extraReplaceCreative: ParamsFor<'replace_creative'> = {
    // @ts-expect-error Empty action params are closed by the OpenAPI contract.
    unlisted_param: true,
  };
  const extraShiftSpend: ParamsFor<'shift_spend'> = {
    // @ts-expect-error Empty action params are closed by the OpenAPI contract.
    unlisted_param: true,
  };
  const extraRollback: ParamsFor<'rollback'> = {
    // @ts-expect-error Empty action params are closed by the OpenAPI contract.
    unlisted_param: true,
  };
  const extraCreateCampaign: ParamsFor<'create_campaign'> = {
    // @ts-expect-error Empty action params are closed by the OpenAPI contract.
    unlisted_param: true,
  };
  const extraCreateAdSet: ParamsFor<'create_ad_set'> = {
    // @ts-expect-error Empty action params are closed by the OpenAPI contract.
    unlisted_param: true,
  };
  const extraCreateAd: ParamsFor<'create_ad'> = {
    // @ts-expect-error Empty action params are closed by the OpenAPI contract.
    unlisted_param: true,
  };
  const extraUploadAsset: ParamsFor<'upload_asset'> = {
    staged_asset_id: 'asset-1',
    asset_type: 'image',
    filename: 'creative.png',
    content_sha256: 'a'.repeat(64),
    // @ts-expect-error Action params are closed by the OpenAPI contract.
    unlisted_param: true,
  };
  const extraAdjustBudget: ParamsFor<'adjust_budget'> = {
    new_daily_budget_minor: 100,
    // @ts-expect-error Action params are closed by the OpenAPI contract.
    unlisted_param: true,
  };
  const extraSetStatus: ParamsFor<'set_status'> = {
    status: 'paused',
    // @ts-expect-error Action params are closed by the OpenAPI contract.
    unlisted_param: true,
  };
  const extraDuplicateAdWithCreative: ParamsFor<'duplicate_ad_with_creative'> = {
    asset_id: 'asset-1',
    status: 'paused',
    // @ts-expect-error Action params are closed by the OpenAPI contract.
    unlisted_param: true,
  };

  const variableParams = { new_daily_budget_minor: 100, unlisted_param: true };
  const bodyWithVariableParams = {
    actions: [{
      type: 'increase_budget' as const,
      target_entity: { type: 'campaign' as const, id: 'campaign-1' },
      params: variableParams,
      rationale: 'Increase the campaign budget.',
    }],
    rationale: 'Increase the campaign budget.',
    idempotency_key: 'closed-params-variable-test',
    evidence: [],
    target_source: 'human_supplied' as const,
  };
  // @ts-expect-error Curated operations reject excess params on retained variable types.
  actionsApiPropose({ path: { workspace: 1 }, body: bodyWithVariableParams });
  // @ts-expect-error The dry-run signature derives the same exact params from the spec.
  actionsApiDryRun({ path: { workspace: 1 }, body: bodyWithVariableParams });
  const validBody: ActionProposalInput = {
    actions: [],
    rationale: 'No action preview.',
    idempotency_key: 'generic-return-type-test',
    evidence: [],
    target_source: 'human_supplied',
  };
  const curatedProposalResult = actionsApiPropose<true>({ path: { workspace: 1 }, body: validBody });
  const generatedProposalResult = generatedActionsApiPropose<true>({ path: { workspace: 1 }, body: validBody });
  expectTypeOf(curatedProposalResult).toEqualTypeOf(generatedProposalResult);
  const curatedDryRunResult = actionsApiDryRun<true>({ path: { workspace: 1 }, body: validBody });
  const generatedDryRunResult = generatedActionsApiDryRun<true>({ path: { workspace: 1 }, body: validBody });
  expectTypeOf(curatedDryRunResult).toEqualTypeOf(generatedDryRunResult);
  void [
    extraIncreaseBudget,
    extraDecreaseBudget,
    extraPause,
    extraResume,
    extraReplaceCreative,
    extraShiftSpend,
    extraRollback,
    extraCreateCampaign,
    extraCreateAdSet,
    extraCreateAd,
    extraUploadAsset,
    extraAdjustBudget,
    extraSetStatus,
    extraDuplicateAdWithCreative,
    variableParams,
    curatedProposalResult,
    curatedDryRunResult,
  ];
}

describe('retryable proposal refusals', () => {
  it.each(['proposal_not_recorded', 'workspace_lock_timeout'] as const)(
    'exposes %s as a typed 503 with Retry-After on both proposal endpoints',
    async (code) => {
      const envelope = { error: { code, message: 'Retry the proposal.' } };
      const fetchMock = vi.fn<typeof globalThis.fetch>(async () =>
        new Response(JSON.stringify(envelope), {
          status: 503,
          headers: { 'Content-Type': 'application/json', 'Retry-After': '1' },
        }),
      );
      configurePlainrouter({
        signalTrackerSecret: 'proposal-test-token',
        baseUrl: 'https://example.test/api/v1',
        fetch: fetchMock,
      });

      const results = [
        await actionsApiPropose({
          path: { workspace: 1 },
          body: {
            actions: [], evidence: [], rationale: 'Pause the ad.',
            idempotency_key: 'retry-test', target_source: 'human_supplied',
          },
        }),
        await launchPlansExecute({
          path: { workspace: 1, deployment_plan: 'plan-test' },
          body: { review_version: 'review-test' },
        }),
      ];
      for (const result of results) {
        if (!result.response) {
          throw new Error("Expected an HTTP response.");
        }
        expect(result.response.status).toBe(503);
        expect(result.response.headers.get('Retry-After')).toBe('1');
        expect(zProposalUnavailable.parse(result.error)).toEqual(envelope);
        expect(isRetryableProposalError(result.response.status, result.error)).toBe(true);
        if (isRetryableProposalError(result.response.status, result.error)) {
          expectTypeOf(result.error).toEqualTypeOf<ProposalUnavailable>();
          expect(result.error.error.code).toBe(code);
        }
      }
      expect(fetchMock).toHaveBeenCalledTimes(2);
    },
  );

  it('does not classify unrelated or malformed errors as retryable proposal refusals', () => {
    const envelope = { error: { code: 'proposal_not_recorded', message: 'Retry.' } };
    expect(isRetryableProposalError(422, envelope)).toBe(false);
    expect(isRetryableProposalError(503, { error: { code: 'unknown', message: 'Failed.' } })).toBe(false);
    expect(isRetryableProposalError(503, { error: { code: 'proposal_not_recorded' } })).toBe(false);
  });
});


describe('copy retry classification', () => {
  it.each(['workspace_lock_timeout', 'proposal_not_recorded'] as const)(
    'classifies %s and preserves Retry-After when present',
    async (code) => {
      for (const retryAfter of ['1', 'Wed, 14 Oct 2026 12:00:00 GMT', undefined]) {
        const envelope = { error: { code, message: 'Retry the proposal.' } };
        configurePlainrouter({
          signalTrackerSecret: 'proposal-test-token',
          baseUrl: 'https://example.test/api/v1',
          fetch: async () => new Response(JSON.stringify(envelope), {
            status: 503,
            headers: {
              'Content-Type': 'application/json',
              ...(retryAfter === undefined ? {} : { 'Retry-After': retryAfter }),
            },
          }),
        });
        const result = await launchPlansCopy({ path: { workspace: 1, deployment_plan: 'failed-plan' } });
        expect(result.response?.status).toBe(503);
        expect(result.error).toEqual(envelope);
        expect(isRetryableProposalError(503, result.error)).toBe(true);
        expect(result.response?.headers.get('Retry-After')).toBe(retryAfter ?? null);
      }
    },
  );
});
