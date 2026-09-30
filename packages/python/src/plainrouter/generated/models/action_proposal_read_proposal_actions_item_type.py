from enum import Enum


class ActionProposalReadProposalActionsItemType(str, Enum):
    ADJUST_BUDGET = "adjust_budget"
    CREATE_AD = "create_ad"
    CREATE_AD_SET = "create_ad_set"
    CREATE_CAMPAIGN = "create_campaign"
    DECREASE_BUDGET = "decrease_budget"
    DUPLICATE_ADSET = "duplicate_adset"
    DUPLICATE_AD_WITH_CREATIVE = "duplicate_ad_with_creative"
    DUPLICATE_AD_WITH_CREATIVE_V2 = "duplicate_ad_with_creative_v2"
    INCREASE_BUDGET = "increase_budget"
    PAUSE = "pause"
    REPLACE_CREATIVE = "replace_creative"
    RESUME = "resume"
    ROLLBACK = "rollback"
    SET_STATUS = "set_status"
    SHIFT_SPEND = "shift_spend"
    UPLOAD_ASSET = "upload_asset"

    def __str__(self) -> str:
        return str(self.value)
