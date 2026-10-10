from enum import Enum


class GetInventoryMetricsResponse200ObjectMetricsItemLevel(str, Enum):
    AD = "ad"
    ADSET = "adset"
    CAMPAIGN = "campaign"

    def __str__(self) -> str:
        return str(self.value)
