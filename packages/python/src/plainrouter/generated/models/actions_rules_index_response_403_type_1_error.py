from enum import Enum


class ActionsRulesIndexResponse403Type1Error(str, Enum):
    INSUFFICIENT_SCOPE = "insufficient_scope"

    def __str__(self) -> str:
        return str(self.value)
