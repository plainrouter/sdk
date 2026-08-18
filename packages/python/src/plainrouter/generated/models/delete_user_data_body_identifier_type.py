from enum import Enum


class DeleteUserDataBodyIdentifierType(str, Enum):
    EMAIL = "email"
    EXTERNAL_ID = "external_id"
    PHONE = "phone"

    def __str__(self) -> str:
        return str(self.value)
