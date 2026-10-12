from enum import Enum


class CreativeMcpPreviewMimeType(str, Enum):
    IMAGEJPEG = "image/jpeg"

    def __str__(self) -> str:
        return str(self.value)
