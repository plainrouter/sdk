from enum import Enum


class ActionProposalReadProposalStatus(str, Enum):
    APPROVED = "approved"
    APPROVED_WITHOUT_EXECUTION = "approved_without_execution"
    AUTO_APPROVED = "auto_approved"
    BLOCKED = "blocked"
    COMPENSATING = "compensating"
    COMPLETED = "completed"
    EXECUTED_PENDING_VERIFICATION = "executed_pending_verification"
    EXECUTING = "executing"
    FAILED = "failed"
    HALTED = "halted"
    MEASURING = "measuring"
    PENDING = "pending"
    REJECTED = "rejected"
    ROLLBACK_INCOMPLETE = "rollback_incomplete"
    ROLLED_BACK = "rolled_back"

    def __str__(self) -> str:
        return str(self.value)
