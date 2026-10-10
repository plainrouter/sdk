from enum import Enum


class IngestionWarningCode(str, Enum):
    CONSENT_CAPTURED_AT_INVALID = "consent_captured_at_invalid"
    EVENT_SOURCE_INVALID = "event_source_invalid"

    def __str__(self) -> str:
        return str(self.value)
