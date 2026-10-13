from enum import Enum


class LaunchCreativesIndexResponse200CreativesDataItemType(str, Enum):
    IMAGE = "image"
    VIDEO = "video"

    def __str__(self) -> str:
        return str(self.value)
