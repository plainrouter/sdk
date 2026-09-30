from enum import Enum


class ActionProposalInputActionsItemType2Type(str, Enum):
    PAUSE = "pause"

    def __str__(self) -> str:
        return str(self.value)
