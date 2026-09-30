from enum import Enum


class ActionProposalInputActionsItemType10Type(str, Enum):
    UPLOAD_ASSET = "upload_asset"

    def __str__(self) -> str:
        return str(self.value)
