from enum import Enum


class ActionPolicyReadDataExecutionMode(str, Enum):
    ASK = "ask"
    FULL = "full"

    def __str__(self) -> str:
        return str(self.value)
