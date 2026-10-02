from enum import Enum


class ProposalReplayConflictMessage(str, Enum):
    IDEMPOTENCY_KEY_PARAMETERS_MISMATCH_THIS_SUBMISSION_KEY_BELONGS_TO_A_DIFFERENT_PROPOSAL = (
        "idempotency_key_parameters_mismatch: This submission key belongs to a different proposal."
    )

    def __str__(self) -> str:
        return str(self.value)
