from enum import Enum


class AgentCredentialErrorError(str, Enum):
    INSUFFICIENT_SCOPE = "insufficient_scope"
    INVALID_TOKEN = "invalid_token"

    def __str__(self) -> str:
        return str(self.value)
