from enum import Enum


class CreateEventResponse202WarningsItemField(str, Enum):
    CONSENT_CAPTURED_AT = "consent.captured_at"
    EVENT_SOURCE = "event_source"

    def __str__(self) -> str:
        return str(self.value)
