from enum import Enum


class AdTestReadVerdictType0MembersItemState(str, Enum):
    FACTS_UNAVAILABLE = "facts_unavailable"
    HALTED = "halted"
    INSUFFICIENT = "insufficient"
    NOT_DELIVERED = "not_delivered"
    RANKED = "ranked"

    def __str__(self) -> str:
        return str(self.value)
