from enum import Enum


class ActionRuleWriteReadRuleRevisionsItemAuthorType(str, Enum):
    AGENT = "agent"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
