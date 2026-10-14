from enum import Enum


class ActionsRulesStoreBodyDefinitionType1TargetLevel(str, Enum):
    AD_SET = "ad_set"
    CAMPAIGN = "campaign"

    def __str__(self) -> str:
        return str(self.value)
