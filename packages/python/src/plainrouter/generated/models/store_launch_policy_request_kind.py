from enum import Enum


class StoreLaunchPolicyRequestKind(str, Enum):
    NAMING = "naming"
    UTM = "utm"

    def __str__(self) -> str:
        return str(self.value)
