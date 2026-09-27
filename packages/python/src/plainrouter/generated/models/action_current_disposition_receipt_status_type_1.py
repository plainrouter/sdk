from enum import Enum


class ActionCurrentDispositionReceiptStatusType1(str, Enum):
    ATTEMPTING = "attempting"
    COMMITTED = "committed"
    COMPENSATED = "compensated"
    COMPENSATING = "compensating"
    COMPENSATION_FAILED = "compensation_failed"
    EXECUTED_PENDING_VERIFICATION = "executed_pending_verification"
    FAILED = "failed"
    IRREVERSIBLE = "irreversible"
    MEASURING = "measuring"
    PENDING = "pending"
    RECONCILIATION_EXHAUSTED = "reconciliation_exhausted"
    RECONCILIATION_REQUIRED = "reconciliation_required"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
