from enum import Enum


class ActionCurrentDispositionOutcomePayloadType0InverseStatus(str, Enum):
    INVERSE_NOT_PROPOSED = "inverse_not_proposed"
    PROPOSED = "proposed"

    def __str__(self) -> str:
        return str(self.value)
