from enum import Enum


class ActionRuleDetailReadRuleRevisionsItemAction(str, Enum):
    DECREASE_BUDGET = "decrease_budget"
    INCREASE_BUDGET = "increase_budget"
    PAUSE = "pause"

    def __str__(self) -> str:
        return str(self.value)
