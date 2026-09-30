from enum import Enum


class ActionProposalInputActionsItemType0TargetEntityType(str, Enum):
    AD = "ad"
    AD_ACCOUNT = "ad_account"
    AD_SET = "ad_set"
    CAMPAIGN = "campaign"

    def __str__(self) -> str:
        return str(self.value)
