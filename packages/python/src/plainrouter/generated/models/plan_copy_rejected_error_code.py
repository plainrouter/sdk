from enum import Enum


class PlanCopyRejectedErrorCode(str, Enum):
    PLAN_NOT_FAILED = "plan_not_failed"
    PLAN_NOT_FOUND = "plan_not_found"
    PLATFORM_AD_ACCOUNT_UNAVAILABLE = "platform_ad_account_unavailable"

    def __str__(self) -> str:
        return str(self.value)
