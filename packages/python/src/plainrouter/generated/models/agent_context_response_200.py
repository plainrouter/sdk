from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_context_response_200_agent import AgentContextResponse200Agent
    from ..models.agent_context_response_200_platform_ad_account_type_0 import (
        AgentContextResponse200PlatformAdAccountType0,
    )


T = TypeVar("T", bound="AgentContextResponse200")


@_attrs_define
class AgentContextResponse200:
    """
    Attributes:
        meta_connected (bool):
        agent (AgentContextResponse200Agent):
        platform_ad_account (AgentContextResponse200PlatformAdAccountType0 | None):
        next_steps (list[str] | Unset): Present only when meta_connected is false.
    """

    meta_connected: bool
    agent: AgentContextResponse200Agent
    platform_ad_account: AgentContextResponse200PlatformAdAccountType0 | None
    next_steps: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_context_response_200_platform_ad_account_type_0 import (
            AgentContextResponse200PlatformAdAccountType0,
        )

        meta_connected = self.meta_connected

        agent = self.agent.to_dict()

        platform_ad_account: dict[str, Any] | None
        if isinstance(self.platform_ad_account, AgentContextResponse200PlatformAdAccountType0):
            platform_ad_account = self.platform_ad_account.to_dict()
        else:
            platform_ad_account = self.platform_ad_account

        next_steps: list[str] | Unset = UNSET
        if not isinstance(self.next_steps, Unset):
            next_steps = self.next_steps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meta_connected": meta_connected,
                "agent": agent,
                "platform_ad_account": platform_ad_account,
            }
        )
        if next_steps is not UNSET:
            field_dict["next_steps"] = next_steps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_context_response_200_agent import AgentContextResponse200Agent
        from ..models.agent_context_response_200_platform_ad_account_type_0 import (
            AgentContextResponse200PlatformAdAccountType0,
        )

        d = dict(src_dict)
        meta_connected = d.pop("meta_connected")

        agent = AgentContextResponse200Agent.from_dict(d.pop("agent"))

        def _parse_platform_ad_account(data: object) -> AgentContextResponse200PlatformAdAccountType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                platform_ad_account_type_0 = AgentContextResponse200PlatformAdAccountType0.from_dict(data)

                return platform_ad_account_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentContextResponse200PlatformAdAccountType0 | None, data)

        platform_ad_account = _parse_platform_ad_account(d.pop("platform_ad_account"))

        next_steps = cast(list[str], d.pop("next_steps", UNSET))

        agent_context_response_200 = cls(
            meta_connected=meta_connected,
            agent=agent,
            platform_ad_account=platform_ad_account,
            next_steps=next_steps,
        )

        agent_context_response_200.additional_properties = d
        return agent_context_response_200

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
