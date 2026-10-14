from enum import Enum


class AgentContextResponse200AgentAuthentication(str, Enum):
    OAUTH2 = "oauth2"
    PERSONAL_ACCESS_TOKEN = "personal_access_token"

    def __str__(self) -> str:
        return str(self.value)
