from enum import Enum


class ActionCurrentDispositionOutcomePayloadType0MetricsType0VerdictType3Type1(str, Enum):
    HELD = "held"
    LOST = "lost"
    NOT_JUDGED = "not_judged"

    def __str__(self) -> str:
        return str(self.value)
