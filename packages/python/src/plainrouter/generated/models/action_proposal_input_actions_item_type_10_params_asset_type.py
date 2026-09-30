from enum import Enum


class ActionProposalInputActionsItemType10ParamsAssetType(str, Enum):
    IMAGE = "image"

    def __str__(self) -> str:
        return str(self.value)
