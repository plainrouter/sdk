from enum import Enum


class ActionReadItemPolicyDecisionType2Type1(str, Enum):
    ALLOW = "allow"
    BLOCK = "block"
    REQUIRE_APPROVAL = "require_approval"

    def __str__(self) -> str:
        return str(self.value)
