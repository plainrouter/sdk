from enum import Enum


class ActionsRulesStoreBodyDefinitionType2Action(str, Enum):
    DECREASE_BUDGET = "decrease_budget"

    def __str__(self) -> str:
        return str(self.value)
