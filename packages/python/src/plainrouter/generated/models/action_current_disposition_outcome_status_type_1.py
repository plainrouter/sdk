from enum import Enum


class ActionCurrentDispositionOutcomeStatusType1(str, Enum):
    MEASURABLE = "measurable"
    NOT_MEASURABLE = "not_measurable"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
