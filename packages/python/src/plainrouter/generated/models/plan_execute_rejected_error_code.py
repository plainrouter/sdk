from enum import Enum


class PlanExecuteRejectedErrorCode(str, Enum):
    AD_SET_DAILY_BUDGET_INVALID = "ad_set_daily_budget_invalid"
    BUDGET_INVALID = "budget_invalid"
    CREATIVE_BYTES_UNAVAILABLE = "creative_bytes_unavailable"
    CREATIVE_NOT_READY = "creative_not_ready"
    CURRENCY_MISMATCH = "currency_mismatch"
    CURRENCY_UNSUPPORTED = "currency_unsupported"
    DEPLOYMENT_PLAN_HAS_NO_ACTIONS = "deployment_plan_has_no_actions"
    DEPLOYMENT_PLAN_NOT_EXECUTABLE = "deployment_plan_not_executable"

    def __str__(self) -> str:
        return str(self.value)
