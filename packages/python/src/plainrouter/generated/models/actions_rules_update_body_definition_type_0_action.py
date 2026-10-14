from enum import Enum


class ActionsRulesUpdateBodyDefinitionType0Action(str, Enum):
    PAUSE = "pause"

    def __str__(self) -> str:
        return str(self.value)
