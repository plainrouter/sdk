from enum import Enum


class ActionProposalInputActionsItemType12Type(str, Enum):
    SET_STATUS = "set_status"

    def __str__(self) -> str:
        return str(self.value)
