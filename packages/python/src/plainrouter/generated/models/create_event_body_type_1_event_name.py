from enum import Enum


class CreateEventBodyType1EventName(str, Enum):
    CONSENT_WITHDRAWAL = "consent_withdrawal"
    SIGNAL_VERIFICATION = "signal_verification"

    def __str__(self) -> str:
        return str(self.value)
