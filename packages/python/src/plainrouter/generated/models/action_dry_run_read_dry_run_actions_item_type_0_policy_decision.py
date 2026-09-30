from enum import Enum


class ActionDryRunReadDryRunActionsItemType0PolicyDecision(str, Enum):
    ALLOW = "allow"
    BLOCK = "block"
    REQUIRE_APPROVAL = "require_approval"

    def __str__(self) -> str:
        return str(self.value)
