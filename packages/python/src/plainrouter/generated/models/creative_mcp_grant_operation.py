from enum import Enum


class CreativeMcpGrantOperation(str, Enum):
    LAUNCH_CREATIVES_INDEX = "launch.creatives.index"
    LAUNCH_CREATIVES_PREVIEW = "launch.creatives.preview"
    LAUNCH_RENDERS_RESUME = "launch.renders.resume"
    LAUNCH_RENDERS_SHOW = "launch.renders.show"
    LAUNCH_RENDERS_STORE = "launch.renders.store"
    LAUNCH_TEMPLATES_INDEX = "launch.templates.index"

    def __str__(self) -> str:
        return str(self.value)
