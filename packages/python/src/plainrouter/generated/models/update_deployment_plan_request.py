from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_deployment_plan_request_budget_type import UpdateDeploymentPlanRequestBudgetType
from ..models.update_deployment_plan_request_platform import UpdateDeploymentPlanRequestPlatform
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_deployment_plan_request_ad_set_spec_type_0 import UpdateDeploymentPlanRequestAdSetSpecType0
    from ..models.update_deployment_plan_request_copy import UpdateDeploymentPlanRequestCopy
    from ..models.update_deployment_plan_request_creative_overrides_item import (
        UpdateDeploymentPlanRequestCreativeOverridesItem,
    )


T = TypeVar("T", bound="UpdateDeploymentPlanRequest")


@_attrs_define
class UpdateDeploymentPlanRequest:
    """
    Attributes:
        name (None | str | Unset):
        platform_ad_account_id (int | Unset):
        platform (UpdateDeploymentPlanRequestPlatform | Unset):
        campaign_ref (None | str | Unset):
        campaign_spec (list[str] | None | Unset):
        ad_set_ref (None | str | Unset):
        ad_set_spec (None | Unset | UpdateDeploymentPlanRequestAdSetSpecType0): Budget fields use positive whole Meta
            minor units. JSON booleans return 422 with field errors; digit-only strings retain their existing normalization.
        budget_type (UpdateDeploymentPlanRequestBudgetType | Unset):
        budget_amount_minor (int | Unset):
        currency (str | Unset):
        copy (UpdateDeploymentPlanRequestCopy | Unset):
        landing_page (str | Unset):
        utm_policy_name (None | str | Unset):
        naming_policy_name (None | str | Unset):
        creative_ids (list[str] | Unset):
        creative_overrides (list[UpdateDeploymentPlanRequestCreativeOverridesItem] | Unset):
    """

    name: None | str | Unset = UNSET
    platform_ad_account_id: int | Unset = UNSET
    platform: UpdateDeploymentPlanRequestPlatform | Unset = UNSET
    campaign_ref: None | str | Unset = UNSET
    campaign_spec: list[str] | None | Unset = UNSET
    ad_set_ref: None | str | Unset = UNSET
    ad_set_spec: None | Unset | UpdateDeploymentPlanRequestAdSetSpecType0 = UNSET
    budget_type: UpdateDeploymentPlanRequestBudgetType | Unset = UNSET
    budget_amount_minor: int | Unset = UNSET
    currency: str | Unset = UNSET
    copy: UpdateDeploymentPlanRequestCopy | Unset = UNSET
    landing_page: str | Unset = UNSET
    utm_policy_name: None | str | Unset = UNSET
    naming_policy_name: None | str | Unset = UNSET
    creative_ids: list[str] | Unset = UNSET
    creative_overrides: list[UpdateDeploymentPlanRequestCreativeOverridesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_deployment_plan_request_ad_set_spec_type_0 import UpdateDeploymentPlanRequestAdSetSpecType0

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        platform_ad_account_id = self.platform_ad_account_id

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        campaign_ref: None | str | Unset
        if isinstance(self.campaign_ref, Unset):
            campaign_ref = UNSET
        else:
            campaign_ref = self.campaign_ref

        campaign_spec: list[str] | None | Unset
        if isinstance(self.campaign_spec, Unset):
            campaign_spec = UNSET
        elif isinstance(self.campaign_spec, list):
            campaign_spec = self.campaign_spec

        else:
            campaign_spec = self.campaign_spec

        ad_set_ref: None | str | Unset
        if isinstance(self.ad_set_ref, Unset):
            ad_set_ref = UNSET
        else:
            ad_set_ref = self.ad_set_ref

        ad_set_spec: dict[str, Any] | None | Unset
        if isinstance(self.ad_set_spec, Unset):
            ad_set_spec = UNSET
        elif isinstance(self.ad_set_spec, UpdateDeploymentPlanRequestAdSetSpecType0):
            ad_set_spec = self.ad_set_spec.to_dict()
        else:
            ad_set_spec = self.ad_set_spec

        budget_type: str | Unset = UNSET
        if not isinstance(self.budget_type, Unset):
            budget_type = self.budget_type.value

        budget_amount_minor = self.budget_amount_minor

        currency = self.currency

        copy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.copy, Unset):
            copy = self.copy.to_dict()

        landing_page = self.landing_page

        utm_policy_name: None | str | Unset
        if isinstance(self.utm_policy_name, Unset):
            utm_policy_name = UNSET
        else:
            utm_policy_name = self.utm_policy_name

        naming_policy_name: None | str | Unset
        if isinstance(self.naming_policy_name, Unset):
            naming_policy_name = UNSET
        else:
            naming_policy_name = self.naming_policy_name

        creative_ids: list[str] | Unset = UNSET
        if not isinstance(self.creative_ids, Unset):
            creative_ids = self.creative_ids

        creative_overrides: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creative_overrides, Unset):
            creative_overrides = []
            for creative_overrides_item_data in self.creative_overrides:
                creative_overrides_item = creative_overrides_item_data.to_dict()
                creative_overrides.append(creative_overrides_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if platform_ad_account_id is not UNSET:
            field_dict["platform_ad_account_id"] = platform_ad_account_id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if campaign_ref is not UNSET:
            field_dict["campaign_ref"] = campaign_ref
        if campaign_spec is not UNSET:
            field_dict["campaign_spec"] = campaign_spec
        if ad_set_ref is not UNSET:
            field_dict["ad_set_ref"] = ad_set_ref
        if ad_set_spec is not UNSET:
            field_dict["ad_set_spec"] = ad_set_spec
        if budget_type is not UNSET:
            field_dict["budget_type"] = budget_type
        if budget_amount_minor is not UNSET:
            field_dict["budget_amount_minor"] = budget_amount_minor
        if currency is not UNSET:
            field_dict["currency"] = currency
        if copy is not UNSET:
            field_dict["copy"] = copy
        if landing_page is not UNSET:
            field_dict["landing_page"] = landing_page
        if utm_policy_name is not UNSET:
            field_dict["utm_policy_name"] = utm_policy_name
        if naming_policy_name is not UNSET:
            field_dict["naming_policy_name"] = naming_policy_name
        if creative_ids is not UNSET:
            field_dict["creative_ids"] = creative_ids
        if creative_overrides is not UNSET:
            field_dict["creative_overrides"] = creative_overrides

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_deployment_plan_request_ad_set_spec_type_0 import UpdateDeploymentPlanRequestAdSetSpecType0
        from ..models.update_deployment_plan_request_copy import UpdateDeploymentPlanRequestCopy
        from ..models.update_deployment_plan_request_creative_overrides_item import (
            UpdateDeploymentPlanRequestCreativeOverridesItem,
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        platform_ad_account_id = d.pop("platform_ad_account_id", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: UpdateDeploymentPlanRequestPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = UpdateDeploymentPlanRequestPlatform(_platform)

        def _parse_campaign_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        campaign_ref = _parse_campaign_ref(d.pop("campaign_ref", UNSET))

        def _parse_campaign_spec(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                campaign_spec_type_0 = cast(list[str], data)

                return campaign_spec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        campaign_spec = _parse_campaign_spec(d.pop("campaign_spec", UNSET))

        def _parse_ad_set_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ad_set_ref = _parse_ad_set_ref(d.pop("ad_set_ref", UNSET))

        def _parse_ad_set_spec(data: object) -> None | Unset | UpdateDeploymentPlanRequestAdSetSpecType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ad_set_spec_type_0 = UpdateDeploymentPlanRequestAdSetSpecType0.from_dict(data)

                return ad_set_spec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateDeploymentPlanRequestAdSetSpecType0, data)

        ad_set_spec = _parse_ad_set_spec(d.pop("ad_set_spec", UNSET))

        _budget_type = d.pop("budget_type", UNSET)
        budget_type: UpdateDeploymentPlanRequestBudgetType | Unset
        if isinstance(_budget_type, Unset):
            budget_type = UNSET
        else:
            budget_type = UpdateDeploymentPlanRequestBudgetType(_budget_type)

        budget_amount_minor = d.pop("budget_amount_minor", UNSET)

        currency = d.pop("currency", UNSET)

        _copy = d.pop("copy", UNSET)
        copy: UpdateDeploymentPlanRequestCopy | Unset
        if isinstance(_copy, Unset):
            copy = UNSET
        else:
            copy = UpdateDeploymentPlanRequestCopy.from_dict(_copy)

        landing_page = d.pop("landing_page", UNSET)

        def _parse_utm_policy_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        utm_policy_name = _parse_utm_policy_name(d.pop("utm_policy_name", UNSET))

        def _parse_naming_policy_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        naming_policy_name = _parse_naming_policy_name(d.pop("naming_policy_name", UNSET))

        creative_ids = cast(list[str], d.pop("creative_ids", UNSET))

        _creative_overrides = d.pop("creative_overrides", UNSET)
        creative_overrides: list[UpdateDeploymentPlanRequestCreativeOverridesItem] | Unset = UNSET
        if _creative_overrides is not UNSET:
            creative_overrides = []
            for creative_overrides_item_data in _creative_overrides:
                creative_overrides_item = UpdateDeploymentPlanRequestCreativeOverridesItem.from_dict(
                    creative_overrides_item_data
                )

                creative_overrides.append(creative_overrides_item)

        update_deployment_plan_request = cls(
            name=name,
            platform_ad_account_id=platform_ad_account_id,
            platform=platform,
            campaign_ref=campaign_ref,
            campaign_spec=campaign_spec,
            ad_set_ref=ad_set_ref,
            ad_set_spec=ad_set_spec,
            budget_type=budget_type,
            budget_amount_minor=budget_amount_minor,
            currency=currency,
            copy=copy,
            landing_page=landing_page,
            utm_policy_name=utm_policy_name,
            naming_policy_name=naming_policy_name,
            creative_ids=creative_ids,
            creative_overrides=creative_overrides,
        )

        update_deployment_plan_request.additional_properties = d
        return update_deployment_plan_request

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
