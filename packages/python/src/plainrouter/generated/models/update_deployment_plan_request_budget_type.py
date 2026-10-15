from enum import Enum


class UpdateDeploymentPlanRequestBudgetType(str, Enum):
    DAILY = "daily"
    LIFETIME = "lifetime"

    def __str__(self) -> str:
        return str(self.value)
