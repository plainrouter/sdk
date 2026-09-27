from enum import Enum


class ActionsApiDryRunBodyTargetSource(str, Enum):
    HUMAN_SUPPLIED = "human_supplied"

    def __str__(self) -> str:
        return str(self.value)
