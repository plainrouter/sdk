from enum import Enum


class ActionRuleWriteReadRuleWindowKind(str, Enum):
    LAST_COMPLETE_DAYS = "last_complete_days"

    def __str__(self) -> str:
        return str(self.value)
