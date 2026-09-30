from enum import Enum


class ActionPolicyReadDataExecutionMode(str, Enum):
    ASK = "ask"
    AUTO_WITH_LIMITS = "auto_with_limits"
    FULL = "full"
    FULL_AUTO = "full_auto"
    SUGGEST_ONLY = "suggest_only"

    def __str__(self) -> str:
        return str(self.value)
