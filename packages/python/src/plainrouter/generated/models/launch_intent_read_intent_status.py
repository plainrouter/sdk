from enum import Enum


class LaunchIntentReadIntentStatus(str, Enum):
    APPROVAL_REQUIRED = "approval_required"
    APPROVED = "approved"
    BLOCKED = "blocked"
    DRIFTED = "drifted"
    EXECUTING = "executing"
    FAILED = "failed"
    PARTIAL = "partial"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
