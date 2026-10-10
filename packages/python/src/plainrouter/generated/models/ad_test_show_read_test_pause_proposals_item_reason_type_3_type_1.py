from enum import Enum


class AdTestShowReadTestPauseProposalsItemReasonType3Type1(str, Enum):
    ADSET_PAUSED = "adset_paused"
    ALREADY_PAUSED = "already_paused"
    ARCHIVED = "archived"
    CAMPAIGN_PAUSED = "campaign_paused"
    DECISION_WINDOW_ELAPSED = "decision_window_elapsed"
    DELETED = "deleted"

    def __str__(self) -> str:
        return str(self.value)
