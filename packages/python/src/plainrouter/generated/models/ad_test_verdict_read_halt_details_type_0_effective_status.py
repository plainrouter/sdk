from enum import Enum


class AdTestVerdictReadHaltDetailsType0EffectiveStatus(str, Enum):
    DISAPPROVED = "DISAPPROVED"
    WITH_ISSUES = "WITH_ISSUES"

    def __str__(self) -> str:
        return str(self.value)
