from enum import Enum


class ActionsRulesStoreBodyDefinitionType2TargetLevel(str, Enum):
    AD_SET = "ad_set"
    CAMPAIGN = "campaign"

    def __str__(self) -> str:
        return str(self.value)
