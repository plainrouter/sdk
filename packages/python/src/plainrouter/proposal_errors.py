from typing import TypeGuard

from .generated.models import ProposalUnavailable, WorkspaceLockTimeout


def is_retryable_proposal_error(
    status_code: int, error: object
) -> TypeGuard[ProposalUnavailable | WorkspaceLockTimeout]:
    """Known 503 proposal refusals may be retried after Response.headers['Retry-After']."""
    return (
        status_code == 503
        and isinstance(error, (ProposalUnavailable, WorkspaceLockTimeout))
        and isinstance(error.error.message, str)
        and error.error.code
        in (
            "proposal_not_recorded",
            "workspace_lock_timeout",
        )
    )
