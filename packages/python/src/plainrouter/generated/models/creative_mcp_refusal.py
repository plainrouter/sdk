from enum import Enum


class CreativeMcpRefusal(str, Enum):
    INSUFFICIENT_SCOPE = "insufficient_scope"
    INVALID_ARGUMENTS = "invalid_arguments"
    INVALID_TOKEN = "invalid_token"
    NOT_FOUND = "not_found"
    RATE_LIMITED = "rate_limited"
    REQUEST_KEY_CONFLICT = "request_key_conflict"
    WORKSPACE_REQUIRED = "workspace_required"

    def __str__(self) -> str:
        return str(self.value)
