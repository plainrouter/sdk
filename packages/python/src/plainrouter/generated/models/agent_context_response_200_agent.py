from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_context_response_200_agent_authentication import AgentContextResponse200AgentAuthentication

T = TypeVar("T", bound="AgentContextResponse200Agent")


@_attrs_define
class AgentContextResponse200Agent:
    """
    Attributes:
        id (str):
        name (str):
        scopes (list[str]):
        authentication (AgentContextResponse200AgentAuthentication):
    """

    id: str
    name: str
    scopes: list[str]
    authentication: AgentContextResponse200AgentAuthentication
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        scopes = self.scopes

        authentication = self.authentication.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "scopes": scopes,
                "authentication": authentication,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        scopes = cast(list[str], d.pop("scopes"))

        authentication = AgentContextResponse200AgentAuthentication(d.pop("authentication"))

        agent_context_response_200_agent = cls(
            id=id,
            name=name,
            scopes=scopes,
            authentication=authentication,
        )

        agent_context_response_200_agent.additional_properties = d
        return agent_context_response_200_agent

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
