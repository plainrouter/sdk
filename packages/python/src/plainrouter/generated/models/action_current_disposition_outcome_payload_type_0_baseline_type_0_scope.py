from enum import Enum


class ActionCurrentDispositionOutcomePayloadType0BaselineType0Scope(str, Enum):
    REST_OF_ACCOUNT = "rest_of_account"
    TARGET = "target"

    def __str__(self) -> str:
        return str(self.value)
