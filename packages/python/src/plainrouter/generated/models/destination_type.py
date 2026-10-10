from enum import Enum


class DestinationType(str, Enum):
    GOOGLE_ADS = "google_ads"
    META = "meta"

    def __str__(self) -> str:
        return str(self.value)
