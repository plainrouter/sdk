from enum import Enum


class ActionProposalInputActionsItemType4Type(str, Enum):
    REPLACE_CREATIVE = "replace_creative"

    def __str__(self) -> str:
        return str(self.value)
