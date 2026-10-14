from enum import Enum


class ActionRuleWriteReadRuleCurrentRevisionTargetLevel(str, Enum):
    AD = "ad"
    AD_SET = "ad_set"
    CAMPAIGN = "campaign"

    def __str__(self) -> str:
        return str(self.value)
