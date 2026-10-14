from enum import Enum


class ActionRuleWriteReadRuleRevisionsItemCostComparison(str, Enum):
    AT_LEAST = "at_least"
    AT_MOST = "at_most"

    def __str__(self) -> str:
        return str(self.value)
