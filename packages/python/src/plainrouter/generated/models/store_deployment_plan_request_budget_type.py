from enum import Enum


class StoreDeploymentPlanRequestBudgetType(str, Enum):
    DAILY = "daily"
    LIFETIME = "lifetime"

    def __str__(self) -> str:
        return str(self.value)
