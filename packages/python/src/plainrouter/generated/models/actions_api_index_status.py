from enum import Enum


class ActionsApiIndexStatus(str, Enum):
    APPROVED_WITHOUT_EXECUTION = "approved_without_execution"
    BLOCKED = "blocked"
    COMPENSATING = "compensating"
    EXECUTED_PENDING_VERIFICATION = "executed_pending_verification"
    EXECUTING = "executing"
    EXECUTION_UNCERTAIN = "execution_uncertain"
    FAILED = "failed"
    MEASURING = "measuring"
    PENDING = "pending"
    REJECTED = "rejected"
    ROLLED_BACK = "rolled_back"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
