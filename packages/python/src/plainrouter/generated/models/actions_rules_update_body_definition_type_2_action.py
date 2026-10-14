from enum import Enum


class ActionsRulesUpdateBodyDefinitionType2Action(str, Enum):
    DECREASE_BUDGET = "decrease_budget"

    def __str__(self) -> str:
        return str(self.value)
