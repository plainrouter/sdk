from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.agent_context_response_200_platform_ad_account_type_0_workspace import (
        AgentContextResponse200PlatformAdAccountType0Workspace,
    )


T = TypeVar("T", bound="AgentContextResponse200PlatformAdAccountType0")


@_attrs_define
class AgentContextResponse200PlatformAdAccountType0:
    """
    Attributes:
        id (int):
        external_id (str):
        name (str):
        platform (str):
        currency (None | str):
        timezone (None | str):
        workspace (AgentContextResponse200PlatformAdAccountType0Workspace):
    """

    id: int
    external_id: str
    name: str
    platform: str
    currency: None | str
    timezone: None | str
    workspace: AgentContextResponse200PlatformAdAccountType0Workspace
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        external_id = self.external_id

        name = self.name

        platform = self.platform

        currency: None | str
        currency = self.currency

        timezone: None | str
        timezone = self.timezone

        workspace = self.workspace.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "external_id": external_id,
                "name": name,
                "platform": platform,
                "currency": currency,
                "timezone": timezone,
                "workspace": workspace,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_context_response_200_platform_ad_account_type_0_workspace import (
            AgentContextResponse200PlatformAdAccountType0Workspace,
        )

        d = dict(src_dict)
        id = d.pop("id")

        external_id = d.pop("external_id")

        name = d.pop("name")

        platform = d.pop("platform")

        def _parse_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency = _parse_currency(d.pop("currency"))

        def _parse_timezone(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        timezone = _parse_timezone(d.pop("timezone"))

        workspace = AgentContextResponse200PlatformAdAccountType0Workspace.from_dict(d.pop("workspace"))

        agent_context_response_200_platform_ad_account_type_0 = cls(
            id=id,
            external_id=external_id,
            name=name,
            platform=platform,
            currency=currency,
            timezone=timezone,
            workspace=workspace,
        )

        agent_context_response_200_platform_ad_account_type_0.additional_properties = d
        return agent_context_response_200_platform_ad_account_type_0

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
