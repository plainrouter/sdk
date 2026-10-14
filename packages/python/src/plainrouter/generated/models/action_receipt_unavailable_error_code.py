from enum import Enum


class ActionReceiptUnavailableErrorCode(str, Enum):
    RECEIPT_NOT_AVAILABLE = "receipt_not_available"

    def __str__(self) -> str:
        return str(self.value)
