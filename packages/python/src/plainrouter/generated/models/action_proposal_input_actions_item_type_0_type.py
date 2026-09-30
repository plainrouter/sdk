from enum import Enum


class ActionProposalInputActionsItemType0Type(str, Enum):
    INCREASE_BUDGET = "increase_budget"

    def __str__(self) -> str:
        return str(self.value)
