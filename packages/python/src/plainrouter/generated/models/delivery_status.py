from enum import Enum


class DeliveryStatus(str, Enum):
    ACCEPTED = "accepted"
    EXPIRED = "expired"
    FAILEDAUTH = "failed:auth"
    FAILEDPERMANENT = "failed:permanent"
    FAILEDUNKNOWN = "failed:unknown"
    QUEUED = "queued"
    RETRYING = "retrying"
    SENT = "sent"
    SKIPPEDCONSENT = "skipped:consent"
    SKIPPEDDUPLICATE = "skipped:duplicate"
    SKIPPEDNO_DESTINATION = "skipped:no_destination"

    def __str__(self) -> str:
        return str(self.value)
