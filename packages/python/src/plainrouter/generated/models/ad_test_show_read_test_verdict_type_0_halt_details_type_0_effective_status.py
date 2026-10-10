from enum import Enum


class AdTestShowReadTestVerdictType0HaltDetailsType0EffectiveStatus(str, Enum):
    DISAPPROVED = "DISAPPROVED"
    WITH_ISSUES = "WITH_ISSUES"

    def __str__(self) -> str:
        return str(self.value)
