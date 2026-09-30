from enum import Enum


class ActionProposalInputActionsItemType3Type(str, Enum):
    RESUME = "resume"

    def __str__(self) -> str:
        return str(self.value)
