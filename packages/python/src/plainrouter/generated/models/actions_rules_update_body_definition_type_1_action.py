from enum import Enum


class ActionsRulesUpdateBodyDefinitionType1Action(str, Enum):
    INCREASE_BUDGET = "increase_budget"

    def __str__(self) -> str:
        return str(self.value)
