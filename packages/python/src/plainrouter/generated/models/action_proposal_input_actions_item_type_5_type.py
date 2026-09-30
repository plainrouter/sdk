from enum import Enum


class ActionProposalInputActionsItemType5Type(str, Enum):
    SHIFT_SPEND = "shift_spend"

    def __str__(self) -> str:
        return str(self.value)
