from enum import Enum


class ActionPolicyResultPhase(str, Enum):
    APPROVAL = "approval"
    EXECUTION = "execution"
    PROPOSAL = "proposal"

    def __str__(self) -> str:
        return str(self.value)
