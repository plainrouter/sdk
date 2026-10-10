from enum import Enum


class CookieDeclarationItemParty(str, Enum):
    FIRST = "first"
    THIRD = "third"

    def __str__(self) -> str:
        return str(self.value)
