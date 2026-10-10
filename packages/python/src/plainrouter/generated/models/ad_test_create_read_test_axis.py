from enum import Enum


class AdTestCreateReadTestAxis(str, Enum):
    ANGLE = "angle"
    FORMAT = "format"
    HOOK = "hook"
    LANDING = "landing"
    OFFER = "offer"
    VISUAL = "visual"

    def __str__(self) -> str:
        return str(self.value)
