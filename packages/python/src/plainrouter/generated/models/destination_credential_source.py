from enum import Enum


class DestinationCredentialSource(str, Enum):
    OAUTH_CONNECTION = "oauth_connection"

    def __str__(self) -> str:
        return str(self.value)
