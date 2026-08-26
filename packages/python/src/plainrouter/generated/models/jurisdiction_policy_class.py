from enum import Enum


class JurisdictionPolicyClass(str, Enum):
    GLOBAL = "global"
    STRICT_EU = "strict_eu"

    def __str__(self) -> str:
        return str(self.value)
