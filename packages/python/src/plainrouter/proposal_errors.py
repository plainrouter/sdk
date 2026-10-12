from typing import TypeGuard

from .generated.models import ProposalUnavailable, ProposalUnavailableErrorCode


def is_retryable_proposal_error(status_code: int, error: object) -> TypeGuard[ProposalUnavailable]:
    """Known 503 proposal refusals may be retried after Response.headers['Retry-After']."""
    return (
        status_code == 503
        and isinstance(error, ProposalUnavailable)
        and error.error.code
        in (
            ProposalUnavailableErrorCode.PROPOSAL_NOT_RECORDED,
            ProposalUnavailableErrorCode.WORKSPACE_LOCK_TIMEOUT,
        )
    )
