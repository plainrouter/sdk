from enum import Enum


class ApiRouteNotFoundErrorCode(str, Enum):
    API_ROUTE_NOT_FOUND = "api_route_not_found"

    def __str__(self) -> str:
        return str(self.value)
