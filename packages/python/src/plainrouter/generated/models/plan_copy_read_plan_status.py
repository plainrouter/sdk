from enum import Enum


class PlanCopyReadPlanStatus(str, Enum):
    DRAFT = "draft"

    def __str__(self) -> str:
        return str(self.value)
