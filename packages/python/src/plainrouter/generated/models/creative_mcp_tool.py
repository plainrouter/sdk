from enum import Enum


class CreativeMcpTool(str, Enum):
    GET_RENDER = "get_render"
    LIST_CREATIVES = "list_creatives"
    LIST_TEMPLATES = "list_templates"
    PREVIEW_CREATIVES = "preview_creatives"
    RENDER_AD = "render_ad"
    RESUME_RENDER = "resume_render"

    def __str__(self) -> str:
        return str(self.value)
