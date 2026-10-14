from enum import Enum


class ActionsRulesStoreBodyDefinitionType0TargetLevel(str, Enum):
    AD = "ad"
    AD_SET = "ad_set"

    def __str__(self) -> str:
        return str(self.value)
