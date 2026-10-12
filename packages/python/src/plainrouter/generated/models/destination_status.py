from enum import Enum


class DestinationStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    NEEDS_ATTENTION = "needs_attention"

    def __str__(self) -> str:
        return str(self.value)
