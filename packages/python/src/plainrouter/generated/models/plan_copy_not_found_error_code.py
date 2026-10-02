from enum import Enum


class PlanCopyNotFoundErrorCode(str, Enum):
    PLAN_NOT_FOUND = "plan_not_found"

    def __str__(self) -> str:
        return str(self.value)
