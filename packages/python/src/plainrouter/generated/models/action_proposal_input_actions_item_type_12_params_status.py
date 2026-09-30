from enum import Enum


class ActionProposalInputActionsItemType12ParamsStatus(str, Enum):
    ACTIVE = "active"
    PAUSED = "paused"

    def __str__(self) -> str:
        return str(self.value)
