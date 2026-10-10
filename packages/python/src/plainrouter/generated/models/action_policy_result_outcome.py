from enum import Enum


class ActionPolicyResultOutcome(str, Enum):
    ALLOWED = "allowed"
    APPROVAL_REQUIRED = "approval_required"
    BLOCKED = "blocked"

    def __str__(self) -> str:
        return str(self.value)
