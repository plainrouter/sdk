from enum import Enum


class LauncherFileImportResponse422Type1Error(str, Enum):
    FILE_IMPORT_REJECTED = "file_import_rejected"

    def __str__(self) -> str:
        return str(self.value)
