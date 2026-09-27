from enum import Enum


class ActionCurrentDispositionRecoveryDispositionType1(str, Enum):
    CONTRADICTORY = "contradictory"
    IRREVERSIBLE = "irreversible"
    NO_COMPENSATION = "no_compensation"
    RESTORED = "restored"
    UNCERTAIN = "uncertain"
    UNRESTORED = "unrestored"

    def __str__(self) -> str:
        return str(self.value)
