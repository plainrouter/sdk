from enum import Enum


class UpdateCreativeStatusRequestStatus(str, Enum):
    APPROVED = "approved"
    DRAFT = "draft"
    RETIRED = "retired"

    def __str__(self) -> str:
        return str(self.value)
