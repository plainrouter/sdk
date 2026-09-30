from enum import Enum


class ActionDryRunReadDryRunActionsItemType1Status(str, Enum):
    DRY_RUN_UNAVAILABLE = "dry_run_unavailable"

    def __str__(self) -> str:
        return str(self.value)
