from enum import Enum


class ActionProposalInputActionsItemType8Type(str, Enum):
    CREATE_AD_SET = "create_ad_set"

    def __str__(self) -> str:
        return str(self.value)
