from enum import Enum


class ActionProposalInputTargetSource(str, Enum):
    HUMAN_SUPPLIED = "human_supplied"

    def __str__(self) -> str:
        return str(self.value)
