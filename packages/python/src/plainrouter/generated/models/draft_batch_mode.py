from enum import Enum


class DraftBatchMode(str, Enum):
    ADD_TO_ADSET = "add_to_adset"
    DUPLICATE_ADSET = "duplicate_adset"
    DUPLICATE_ADSET_PER_MEDIA = "duplicate_adset_per_media"

    def __str__(self) -> str:
        return str(self.value)
