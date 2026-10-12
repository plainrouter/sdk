from enum import Enum


class ProposalUnavailableErrorCode(str, Enum):
    PROPOSAL_NOT_RECORDED = "proposal_not_recorded"
    WORKSPACE_LOCK_TIMEOUT = "workspace_lock_timeout"

    def __str__(self) -> str:
        return str(self.value)
