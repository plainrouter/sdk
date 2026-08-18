from enum import Enum


class DestinationType(str, Enum):
    META = "meta"

    def __str__(self) -> str:
        return str(self.value)
