from enum import Enum


class UpdateDeploymentPlanRequestCopyCta(str, Enum):
    LEARN_MORE = "learn_more"
    SHOP_NOW = "shop_now"
    SIGN_UP = "sign_up"

    def __str__(self) -> str:
        return str(self.value)
