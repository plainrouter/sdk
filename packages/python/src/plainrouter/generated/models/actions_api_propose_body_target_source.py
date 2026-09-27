from enum import Enum


class ActionsApiProposeBodyTargetSource(str, Enum):
    HUMAN_SUPPLIED = "human_supplied"

    def __str__(self) -> str:
        return str(self.value)
