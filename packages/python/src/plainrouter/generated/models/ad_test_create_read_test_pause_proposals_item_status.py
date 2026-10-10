from enum import Enum


class AdTestCreateReadTestPauseProposalsItemStatus(str, Enum):
    EXPIRED = "expired"
    PENDING = "pending"
    PROPOSED = "proposed"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
