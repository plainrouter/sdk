from enum import Enum


class ActionProposalInputActionsItemType6Type(str, Enum):
    ROLLBACK = "rollback"

    def __str__(self) -> str:
        return str(self.value)
