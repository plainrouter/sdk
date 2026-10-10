from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeploymentPlan")


@_attrs_define
class DeploymentPlan:
    """
    Attributes:
        id (str):
        workspace_id (int):
        platform_ad_account_id (int):
        platform (str):
        campaign_ref (None | str):
        campaign_spec (list[Any] | None):
        ad_set_ref (None | str):
        ad_set_spec (list[Any] | None): When present, bid_amount must be a positive integer in Meta minor units for the
            account currency. Digit-only strings of at most 18 digits are accepted and normalized to integers. Null, zero,
            negatives, decimals and other strings are refused on ad_set_spec.bid_amount.
        budget_type (str):
        budget_amount_minor (int):
        currency (str):
        copy (list[Any]):
        landing_page (str):
        utm_policy_id (None | str):
        naming_policy_id (None | str):
        status (str):
        validation_result (list[Any] | None):
        diff (list[Any] | None):
        validated_at (datetime.datetime | None):
        approval_id (None | str):
        created_at (datetime.datetime | None):
        updated_at (datetime.datetime | None):
        platform_object_ids (list[Any]):
        name (None | str):
    """

    id: str
    workspace_id: int
    platform_ad_account_id: int
    platform: str
    campaign_ref: None | str
    campaign_spec: list[Any] | None
    ad_set_ref: None | str
    ad_set_spec: list[Any] | None
    budget_type: str
    budget_amount_minor: int
    currency: str
    copy: list[Any]
    landing_page: str
    utm_policy_id: None | str
    naming_policy_id: None | str
    status: str
    validation_result: list[Any] | None
    diff: list[Any] | None
    validated_at: datetime.datetime | None
    approval_id: None | str
    created_at: datetime.datetime | None
    updated_at: datetime.datetime | None
    platform_object_ids: list[Any]
    name: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workspace_id = self.workspace_id

        platform_ad_account_id = self.platform_ad_account_id

        platform = self.platform

        campaign_ref: None | str
        campaign_ref = self.campaign_ref

        campaign_spec: list[Any] | None
        if isinstance(self.campaign_spec, list):
            campaign_spec = self.campaign_spec

        else:
            campaign_spec = self.campaign_spec

        ad_set_ref: None | str
        ad_set_ref = self.ad_set_ref

        ad_set_spec: list[Any] | None
        if isinstance(self.ad_set_spec, list):
            ad_set_spec = self.ad_set_spec

        else:
            ad_set_spec = self.ad_set_spec

        budget_type = self.budget_type

        budget_amount_minor = self.budget_amount_minor

        currency = self.currency

        copy = self.copy

        landing_page = self.landing_page

        utm_policy_id: None | str
        utm_policy_id = self.utm_policy_id

        naming_policy_id: None | str
        naming_policy_id = self.naming_policy_id

        status = self.status

        validation_result: list[Any] | None
        if isinstance(self.validation_result, list):
            validation_result = self.validation_result

        else:
            validation_result = self.validation_result

        diff: list[Any] | None
        if isinstance(self.diff, list):
            diff = self.diff

        else:
            diff = self.diff

        validated_at: None | str
        if isinstance(self.validated_at, datetime.datetime):
            validated_at = self.validated_at.isoformat()
        else:
            validated_at = self.validated_at

        approval_id: None | str
        approval_id = self.approval_id

        created_at: None | str
        if isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        platform_object_ids = self.platform_object_ids

        name: None | str
        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workspace_id": workspace_id,
                "platform_ad_account_id": platform_ad_account_id,
                "platform": platform,
                "campaign_ref": campaign_ref,
                "campaign_spec": campaign_spec,
                "ad_set_ref": ad_set_ref,
                "ad_set_spec": ad_set_spec,
                "budget_type": budget_type,
                "budget_amount_minor": budget_amount_minor,
                "currency": currency,
                "copy": copy,
                "landing_page": landing_page,
                "utm_policy_id": utm_policy_id,
                "naming_policy_id": naming_policy_id,
                "status": status,
                "validation_result": validation_result,
                "diff": diff,
                "validated_at": validated_at,
                "approval_id": approval_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "platform_object_ids": platform_object_ids,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        workspace_id = d.pop("workspace_id")

        platform_ad_account_id = d.pop("platform_ad_account_id")

        platform = d.pop("platform")

        def _parse_campaign_ref(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        campaign_ref = _parse_campaign_ref(d.pop("campaign_ref"))

        def _parse_campaign_spec(data: object) -> list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                campaign_spec_type_0 = cast(list[Any], data)

                return campaign_spec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None, data)

        campaign_spec = _parse_campaign_spec(d.pop("campaign_spec"))

        def _parse_ad_set_ref(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ad_set_ref = _parse_ad_set_ref(d.pop("ad_set_ref"))

        def _parse_ad_set_spec(data: object) -> list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ad_set_spec_type_0 = cast(list[Any], data)

                return ad_set_spec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None, data)

        ad_set_spec = _parse_ad_set_spec(d.pop("ad_set_spec"))

        budget_type = d.pop("budget_type")

        budget_amount_minor = d.pop("budget_amount_minor")

        currency = d.pop("currency")

        copy = cast(list[Any], d.pop("copy"))

        landing_page = d.pop("landing_page")

        def _parse_utm_policy_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        utm_policy_id = _parse_utm_policy_id(d.pop("utm_policy_id"))

        def _parse_naming_policy_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        naming_policy_id = _parse_naming_policy_id(d.pop("naming_policy_id"))

        status = d.pop("status")

        def _parse_validation_result(data: object) -> list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                validation_result_type_0 = cast(list[Any], data)

                return validation_result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None, data)

        validation_result = _parse_validation_result(d.pop("validation_result"))

        def _parse_diff(data: object) -> list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                diff_type_0 = cast(list[Any], data)

                return diff_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None, data)

        diff = _parse_diff(d.pop("diff"))

        def _parse_validated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                validated_at_type_0 = datetime.datetime.fromisoformat(data)

                return validated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        validated_at = _parse_validated_at(d.pop("validated_at"))

        def _parse_approval_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        approval_id = _parse_approval_id(d.pop("approval_id"))

        def _parse_created_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        created_at = _parse_created_at(d.pop("created_at"))

        def _parse_updated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        platform_object_ids = cast(list[Any], d.pop("platform_object_ids"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        deployment_plan = cls(
            id=id,
            workspace_id=workspace_id,
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
            utm_policy_id=utm_policy_id,
            naming_policy_id=naming_policy_id,
            status=status,
            validation_result=validation_result,
            diff=diff,
            validated_at=validated_at,
            approval_id=approval_id,
            created_at=created_at,
            updated_at=updated_at,
            platform_object_ids=platform_object_ids,
            name=name,
        )

        deployment_plan.additional_properties = d
        return deployment_plan

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
