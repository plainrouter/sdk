import type { ProposalUnavailable } from './generated/types.gen.js';
import { zProposalUnavailable } from './generated/zod.gen.js';

/** Known 503 proposal refusals may be retried after the response's Retry-After header. */
export const isRetryableProposalError = (
  status: number,
  error: unknown,
): error is ProposalUnavailable =>
  status === 503 && zProposalUnavailable.safeParse(error).success;
