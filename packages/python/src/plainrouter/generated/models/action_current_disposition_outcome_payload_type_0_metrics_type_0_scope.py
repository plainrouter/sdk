from enum import Enum


class ActionCurrentDispositionOutcomePayloadType0MetricsType0Scope(str, Enum):
    REST_OF_ACCOUNT = "rest_of_account"
    TARGET = "target"

    def __str__(self) -> str:
        return str(self.value)
