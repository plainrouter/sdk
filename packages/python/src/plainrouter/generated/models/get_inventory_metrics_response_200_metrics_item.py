from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_inventory_metrics_response_200_metrics_item_action_values_type_0 import (
        GetInventoryMetricsResponse200MetricsItemActionValuesType0,
    )
    from ..models.get_inventory_metrics_response_200_metrics_item_actions_type_0 import (
        GetInventoryMetricsResponse200MetricsItemActionsType0,
    )


T = TypeVar("T", bound="GetInventoryMetricsResponse200MetricsItem")


@_attrs_define
class GetInventoryMetricsResponse200MetricsItem:
    """
    Attributes:
        id (int):
        platform_ad_account_id (int):
        ad_external_id (str):
        campaign_external_id (None | str):
        adset_external_id (None | str):
        date (str):
        account_currency (str):
        spend (str):
        impressions (int):
        clicks (int):
        inline_link_clicks (int):
        actions (GetInventoryMetricsResponse200MetricsItemActionsType0 | list[Any] | None):
        action_values (GetInventoryMetricsResponse200MetricsItemActionValuesType0 | list[Any] | None):
        fetched_at (None | str):
        arrivals (int | None):
        creative_id (None | str):
        generator (None | str):
        generator_job (None | str):
        parent_creative (None | str):
    """

    id: int
    platform_ad_account_id: int
    ad_external_id: str
    campaign_external_id: None | str
    adset_external_id: None | str
    date: str
    account_currency: str
    spend: str
    impressions: int
    clicks: int
    inline_link_clicks: int
    actions: GetInventoryMetricsResponse200MetricsItemActionsType0 | list[Any] | None
    action_values: GetInventoryMetricsResponse200MetricsItemActionValuesType0 | list[Any] | None
    fetched_at: None | str
    arrivals: int | None
    creative_id: None | str
    generator: None | str
    generator_job: None | str
    parent_creative: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_inventory_metrics_response_200_metrics_item_action_values_type_0 import (
            GetInventoryMetricsResponse200MetricsItemActionValuesType0,
        )
        from ..models.get_inventory_metrics_response_200_metrics_item_actions_type_0 import (
            GetInventoryMetricsResponse200MetricsItemActionsType0,
        )

        id = self.id

        platform_ad_account_id = self.platform_ad_account_id

        ad_external_id = self.ad_external_id

        campaign_external_id: None | str
        campaign_external_id = self.campaign_external_id

        adset_external_id: None | str
        adset_external_id = self.adset_external_id

        date = self.date

        account_currency = self.account_currency

        spend = self.spend

        impressions = self.impressions

        clicks = self.clicks

        inline_link_clicks = self.inline_link_clicks

        actions: dict[str, Any] | list[Any] | None
        if isinstance(self.actions, GetInventoryMetricsResponse200MetricsItemActionsType0):
            actions = self.actions.to_dict()
        elif isinstance(self.actions, list):
            actions = self.actions

        else:
            actions = self.actions

        action_values: dict[str, Any] | list[Any] | None
        if isinstance(self.action_values, GetInventoryMetricsResponse200MetricsItemActionValuesType0):
            action_values = self.action_values.to_dict()
        elif isinstance(self.action_values, list):
            action_values = self.action_values

        else:
            action_values = self.action_values

        fetched_at: None | str
        fetched_at = self.fetched_at

        arrivals: int | None
        arrivals = self.arrivals

        creative_id: None | str
        creative_id = self.creative_id

        generator: None | str
        generator = self.generator

        generator_job: None | str
        generator_job = self.generator_job

        parent_creative: None | str
        parent_creative = self.parent_creative

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "platform_ad_account_id": platform_ad_account_id,
                "ad_external_id": ad_external_id,
                "campaign_external_id": campaign_external_id,
                "adset_external_id": adset_external_id,
                "date": date,
                "account_currency": account_currency,
                "spend": spend,
                "impressions": impressions,
                "clicks": clicks,
                "inline_link_clicks": inline_link_clicks,
                "actions": actions,
                "action_values": action_values,
                "fetched_at": fetched_at,
                "arrivals": arrivals,
                "creative_id": creative_id,
                "generator": generator,
                "generator_job": generator_job,
                "parent_creative": parent_creative,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_inventory_metrics_response_200_metrics_item_action_values_type_0 import (
            GetInventoryMetricsResponse200MetricsItemActionValuesType0,
        )
        from ..models.get_inventory_metrics_response_200_metrics_item_actions_type_0 import (
            GetInventoryMetricsResponse200MetricsItemActionsType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        platform_ad_account_id = d.pop("platform_ad_account_id")

        ad_external_id = d.pop("ad_external_id")

        def _parse_campaign_external_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        campaign_external_id = _parse_campaign_external_id(d.pop("campaign_external_id"))

        def _parse_adset_external_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        adset_external_id = _parse_adset_external_id(d.pop("adset_external_id"))

        date = d.pop("date")

        account_currency = d.pop("account_currency")

        spend = d.pop("spend")

        impressions = d.pop("impressions")

        clicks = d.pop("clicks")

        inline_link_clicks = d.pop("inline_link_clicks")

        def _parse_actions(data: object) -> GetInventoryMetricsResponse200MetricsItemActionsType0 | list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actions_type_0 = GetInventoryMetricsResponse200MetricsItemActionsType0.from_dict(data)

                return actions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                actions_type_1 = cast(list[Any], data)

                return actions_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetInventoryMetricsResponse200MetricsItemActionsType0 | list[Any] | None, data)

        actions = _parse_actions(d.pop("actions"))

        def _parse_action_values(
            data: object,
        ) -> GetInventoryMetricsResponse200MetricsItemActionValuesType0 | list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_values_type_0 = GetInventoryMetricsResponse200MetricsItemActionValuesType0.from_dict(data)

                return action_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                action_values_type_1 = cast(list[Any], data)

                return action_values_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetInventoryMetricsResponse200MetricsItemActionValuesType0 | list[Any] | None, data)

        action_values = _parse_action_values(d.pop("action_values"))

        def _parse_fetched_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        fetched_at = _parse_fetched_at(d.pop("fetched_at"))

        def _parse_arrivals(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        arrivals = _parse_arrivals(d.pop("arrivals"))

        def _parse_creative_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        creative_id = _parse_creative_id(d.pop("creative_id"))

        def _parse_generator(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        generator = _parse_generator(d.pop("generator"))

        def _parse_generator_job(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        generator_job = _parse_generator_job(d.pop("generator_job"))

        def _parse_parent_creative(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parent_creative = _parse_parent_creative(d.pop("parent_creative"))

        get_inventory_metrics_response_200_metrics_item = cls(
            id=id,
            platform_ad_account_id=platform_ad_account_id,
            ad_external_id=ad_external_id,
            campaign_external_id=campaign_external_id,
            adset_external_id=adset_external_id,
            date=date,
            account_currency=account_currency,
            spend=spend,
            impressions=impressions,
            clicks=clicks,
            inline_link_clicks=inline_link_clicks,
            actions=actions,
            action_values=action_values,
            fetched_at=fetched_at,
            arrivals=arrivals,
            creative_id=creative_id,
            generator=generator,
            generator_job=generator_job,
            parent_creative=parent_creative,
        )

        get_inventory_metrics_response_200_metrics_item.additional_properties = d
        return get_inventory_metrics_response_200_metrics_item

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
