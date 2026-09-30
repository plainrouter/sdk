from enum import Enum


class ActionProposalInputActionsItemType11Type(str, Enum):
    ADJUST_BUDGET = "adjust_budget"

    def __str__(self) -> str:
        return str(self.value)
