from enum import Enum


class CreativeMcpPreviewState(str, Enum):
    PENDING = "pending"
    READY = "ready"
    REFUSED = "refused"

    def __str__(self) -> str:
        return str(self.value)
