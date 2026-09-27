from enum import Enum


class ActionBatchReadDataRestorationSummaryType3Type1(str, Enum):
    ALL_RECEIPTS_COMPENSATED_LATE = "all_receipts_compensated_late"

    def __str__(self) -> str:
        return str(self.value)
