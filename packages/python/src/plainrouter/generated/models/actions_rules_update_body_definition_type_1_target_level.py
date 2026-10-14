from enum import Enum


class ActionsRulesUpdateBodyDefinitionType1TargetLevel(str, Enum):
    AD_SET = "ad_set"
    CAMPAIGN = "campaign"

    def __str__(self) -> str:
        return str(self.value)
