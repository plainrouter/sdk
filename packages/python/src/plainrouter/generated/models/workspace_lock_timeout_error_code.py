from enum import Enum


class WorkspaceLockTimeoutErrorCode(str, Enum):
    WORKSPACE_LOCK_TIMEOUT = "workspace_lock_timeout"

    def __str__(self) -> str:
        return str(self.value)
