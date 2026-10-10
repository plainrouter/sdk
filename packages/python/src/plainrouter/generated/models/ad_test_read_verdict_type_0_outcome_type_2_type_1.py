from enum import Enum


class AdTestReadVerdictType0OutcomeType2Type1(str, Enum):
    HALTED = "halted"
    NOT_JUDGED = "not_judged"
    NO_CLEAR_WINNER = "no_clear_winner"
    WINNER = "winner"

    def __str__(self) -> str:
        return str(self.value)
