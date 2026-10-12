from enum import Enum


class LaunchCreativesIndexResponse200CreativesDataItemStatus(str, Enum):
    APPROVED = "approved"
    DRAFT = "draft"
    RETIRED = "retired"

    def __str__(self) -> str:
        return str(self.value)
