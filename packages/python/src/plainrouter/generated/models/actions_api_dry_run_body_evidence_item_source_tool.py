from enum import Enum


class ActionsApiDryRunBodyEvidenceItemSourceTool(str, Enum):
    GET_ACCOUNT_STATE = "get_account_state"
    GET_CREATIVE_LIBRARY = "get-creative-library"
    GET_PERFORMANCE = "get_performance"
    GET_SIGNAL_HEALTH = "get_signal_health"
    STAGED_ASSET_MANIFEST = "staged-asset-manifest"

    def __str__(self) -> str:
        return str(self.value)
