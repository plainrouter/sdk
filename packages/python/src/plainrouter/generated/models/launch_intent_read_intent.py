from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.launch_intent_read_intent_status import LaunchIntentReadIntentStatus

if TYPE_CHECKING:
    from ..models.launch_intent_read_intent_actions_item import LaunchIntentReadIntentActionsItem


T = TypeVar("T", bound="LaunchIntentReadIntent")


@_attrs_define
class LaunchIntentReadIntent:
    """
    Attributes:
        id (str):
        status (LaunchIntentReadIntentStatus):
        action_batch_id (None | str):
        policy_reasons (list[str]):
        provider_object_ids (Any):
        campaign_id (None | str):
        ad_set_id (None | str):
        currency (None | str):
        actions (list[LaunchIntentReadIntentActionsItem]):
    """

    id: str
    status: LaunchIntentReadIntentStatus
    action_batch_id: None | str
    policy_reasons: list[str]
    provider_object_ids: Any
    campaign_id: None | str
    ad_set_id: None | str
    currency: None | str
    actions: list[LaunchIntentReadIntentActionsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status.value

        action_batch_id: None | str
        action_batch_id = self.action_batch_id

        policy_reasons = self.policy_reasons

        provider_object_ids = self.provider_object_ids

        campaign_id: None | str
        campaign_id = self.campaign_id

        ad_set_id: None | str
        ad_set_id = self.ad_set_id

        currency: None | str
        currency = self.currency

        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()
            actions.append(actions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "action_batch_id": action_batch_id,
                "policy_reasons": policy_reasons,
                "provider_object_ids": provider_object_ids,
                "campaign_id": campaign_id,
                "ad_set_id": ad_set_id,
                "currency": currency,
                "actions": actions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.launch_intent_read_intent_actions_item import LaunchIntentReadIntentActionsItem

        d = dict(src_dict)
        id = d.pop("id")

        status = LaunchIntentReadIntentStatus(d.pop("status"))

        def _parse_action_batch_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        action_batch_id = _parse_action_batch_id(d.pop("action_batch_id"))

        policy_reasons = cast(list[str], d.pop("policy_reasons"))

        provider_object_ids = d.pop("provider_object_ids")

        def _parse_campaign_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        campaign_id = _parse_campaign_id(d.pop("campaign_id"))

        def _parse_ad_set_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ad_set_id = _parse_ad_set_id(d.pop("ad_set_id"))

        def _parse_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency = _parse_currency(d.pop("currency"))

        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = LaunchIntentReadIntentActionsItem.from_dict(actions_item_data)

            actions.append(actions_item)

        launch_intent_read_intent = cls(
            id=id,
            status=status,
            action_batch_id=action_batch_id,
            policy_reasons=policy_reasons,
            provider_object_ids=provider_object_ids,
            campaign_id=campaign_id,
            ad_set_id=ad_set_id,
            currency=currency,
            actions=actions,
        )

        launch_intent_read_intent.additional_properties = d
        return launch_intent_read_intent

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
