from enum import Enum


class UpdateDeploymentPlanRequestPlatform(str, Enum):
    GOOGLE = "google"
    META = "meta"
    MICROSOFT = "microsoft"

    def __str__(self) -> str:
        return str(self.value)
