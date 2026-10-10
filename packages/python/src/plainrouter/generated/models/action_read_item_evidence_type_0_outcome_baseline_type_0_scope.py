from enum import Enum


class ActionReadItemEvidenceType0OutcomeBaselineType0Scope(str, Enum):
    REST_OF_ACCOUNT = "rest_of_account"
    TARGET = "target"

    def __str__(self) -> str:
        return str(self.value)
