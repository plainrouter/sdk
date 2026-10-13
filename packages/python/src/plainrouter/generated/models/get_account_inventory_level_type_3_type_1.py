from enum import Enum


class GetAccountInventoryLevelType3Type1(str, Enum):
    AD = "ad"
    ADSET = "adset"
    CAMPAIGN = "campaign"

    def __str__(self) -> str:
        return str(self.value)
