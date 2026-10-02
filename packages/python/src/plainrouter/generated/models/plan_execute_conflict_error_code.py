from enum import Enum


class PlanExecuteConflictErrorCode(str, Enum):
    LAUNCH_SUBMISSION_KEY_PLAN_MISMATCH = "launch_submission_key_plan_mismatch"

    def __str__(self) -> str:
        return str(self.value)
