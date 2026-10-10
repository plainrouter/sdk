from enum import Enum


class ActionReadItemEvidenceType0OutcomeMetricsType0VerdictType1(str, Enum):
    HELD = "held"
    LOST = "lost"
    NOT_JUDGED = "not_judged"

    def __str__(self) -> str:
        return str(self.value)
