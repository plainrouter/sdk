import { describe, expect, expectTypeOf, it, vi } from 'vitest';

import {
  actionsApiPropose,
  configurePlainrouter,
  isRetryableProposalError,
  launchPlansExecute,
  type ProposalUnavailable,
  zProposalUnavailable,
} from '../src/index.js';

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
