from enum import Enum


class ActionCurrentDispositionOutcomePayloadType0Status(str, Enum):
    MEASURABLE = "measurable"
    NOT_MEASURABLE = "not_measurable"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
