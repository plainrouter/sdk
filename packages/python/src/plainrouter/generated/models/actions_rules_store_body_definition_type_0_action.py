from enum import Enum


class ActionsRulesStoreBodyDefinitionType0Action(str, Enum):
    PAUSE = "pause"

    def __str__(self) -> str:
        return str(self.value)
