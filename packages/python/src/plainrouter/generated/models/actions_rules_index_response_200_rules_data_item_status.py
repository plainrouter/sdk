from enum import Enum


class ActionsRulesIndexResponse200RulesDataItemStatus(str, Enum):
    DISABLED = "disabled"
    ENABLED = "enabled"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
