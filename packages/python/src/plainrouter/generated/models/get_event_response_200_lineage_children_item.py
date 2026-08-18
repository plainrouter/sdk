from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_event_response_200_lineage_children_item_click_ids_type_0 import (
        GetEventResponse200LineageChildrenItemClickIdsType0,
    )
    from ..models.get_event_response_200_lineage_children_item_consent_type_0 import (
        GetEventResponse200LineageChildrenItemConsentType0,
    )
    from ..models.get_event_response_200_lineage_children_item_session_type_0 import (
        GetEventResponse200LineageChildrenItemSessionType0,
    )
    from ..models.get_event_response_200_lineage_children_item_user_data_hashed_type_0 import (
        GetEventResponse200LineageChildrenItemUserDataHashedType0,
    )
    from ..models.get_event_response_200_lineage_children_item_value_data_type_0 import (
        GetEventResponse200LineageChildrenItemValueDataType0,
    )


T = TypeVar("T", bound="GetEventResponse200LineageChildrenItem")


@_attrs_define
class GetEventResponse200LineageChildrenItem:
    """
    Attributes:
        id (str):
        signal_tracker_id (str):
        parent_event_id (None | str):
        event_name (str):
        event_time (str):
        action_source (str):
        event_class (str):
        order_id (None | str):
        value_amount (int | None):
        value_currency (None | str):
        created_at (str):
        consent_basis (str):
        measurement_class (str):
        attribution_join (str):
        enforcement_scope (str):
        consent_normalization_version (str):
        consent (GetEventResponse200LineageChildrenItemConsentType0 | list[Any] | None):
        user_data_hashed (GetEventResponse200LineageChildrenItemUserDataHashedType0 | list[Any] | None):
        click_ids (GetEventResponse200LineageChildrenItemClickIdsType0 | list[Any] | None):
        session (GetEventResponse200LineageChildrenItemSessionType0 | list[Any] | None):
        value_data (GetEventResponse200LineageChildrenItemValueDataType0 | list[Any] | None):
        event_source (None | str):
        payload_expired (bool):
    """

    id: str
    signal_tracker_id: str
    parent_event_id: None | str
    event_name: str
    event_time: str
    action_source: str
    event_class: str
    order_id: None | str
    value_amount: int | None
    value_currency: None | str
    created_at: str
    consent_basis: str
    measurement_class: str
    attribution_join: str
    enforcement_scope: str
    consent_normalization_version: str
    consent: GetEventResponse200LineageChildrenItemConsentType0 | list[Any] | None
    user_data_hashed: GetEventResponse200LineageChildrenItemUserDataHashedType0 | list[Any] | None
    click_ids: GetEventResponse200LineageChildrenItemClickIdsType0 | list[Any] | None
    session: GetEventResponse200LineageChildrenItemSessionType0 | list[Any] | None
    value_data: GetEventResponse200LineageChildrenItemValueDataType0 | list[Any] | None
    event_source: None | str
    payload_expired: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_event_response_200_lineage_children_item_click_ids_type_0 import (
            GetEventResponse200LineageChildrenItemClickIdsType0,
        )
        from ..models.get_event_response_200_lineage_children_item_consent_type_0 import (
            GetEventResponse200LineageChildrenItemConsentType0,
        )
        from ..models.get_event_response_200_lineage_children_item_session_type_0 import (
            GetEventResponse200LineageChildrenItemSessionType0,
        )
        from ..models.get_event_response_200_lineage_children_item_user_data_hashed_type_0 import (
            GetEventResponse200LineageChildrenItemUserDataHashedType0,
        )
        from ..models.get_event_response_200_lineage_children_item_value_data_type_0 import (
            GetEventResponse200LineageChildrenItemValueDataType0,
        )

        id = self.id

        signal_tracker_id = self.signal_tracker_id

        parent_event_id: None | str
        parent_event_id = self.parent_event_id

        event_name = self.event_name

        event_time = self.event_time

        action_source = self.action_source

        event_class = self.event_class

        order_id: None | str
        order_id = self.order_id

        value_amount: int | None
        value_amount = self.value_amount

        value_currency: None | str
        value_currency = self.value_currency

        created_at = self.created_at

        consent_basis = self.consent_basis

        measurement_class = self.measurement_class

        attribution_join = self.attribution_join

        enforcement_scope = self.enforcement_scope

        consent_normalization_version = self.consent_normalization_version

        consent: dict[str, Any] | list[Any] | None
        if isinstance(self.consent, GetEventResponse200LineageChildrenItemConsentType0):
            consent = self.consent.to_dict()
        elif isinstance(self.consent, list):
            consent = self.consent

        else:
            consent = self.consent

        user_data_hashed: dict[str, Any] | list[Any] | None
        if isinstance(self.user_data_hashed, GetEventResponse200LineageChildrenItemUserDataHashedType0):
            user_data_hashed = self.user_data_hashed.to_dict()
        elif isinstance(self.user_data_hashed, list):
            user_data_hashed = self.user_data_hashed

        else:
            user_data_hashed = self.user_data_hashed

        click_ids: dict[str, Any] | list[Any] | None
        if isinstance(self.click_ids, GetEventResponse200LineageChildrenItemClickIdsType0):
            click_ids = self.click_ids.to_dict()
        elif isinstance(self.click_ids, list):
            click_ids = self.click_ids

        else:
            click_ids = self.click_ids

        session: dict[str, Any] | list[Any] | None
        if isinstance(self.session, GetEventResponse200LineageChildrenItemSessionType0):
            session = self.session.to_dict()
        elif isinstance(self.session, list):
            session = self.session

        else:
            session = self.session

        value_data: dict[str, Any] | list[Any] | None
        if isinstance(self.value_data, GetEventResponse200LineageChildrenItemValueDataType0):
            value_data = self.value_data.to_dict()
        elif isinstance(self.value_data, list):
            value_data = self.value_data

        else:
            value_data = self.value_data

        event_source: None | str
        event_source = self.event_source

        payload_expired = self.payload_expired

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "signal_tracker_id": signal_tracker_id,
                "parent_event_id": parent_event_id,
                "event_name": event_name,
                "event_time": event_time,
                "action_source": action_source,
                "event_class": event_class,
                "order_id": order_id,
                "value_amount": value_amount,
                "value_currency": value_currency,
                "created_at": created_at,
                "consent_basis": consent_basis,
                "measurement_class": measurement_class,
                "attribution_join": attribution_join,
                "enforcement_scope": enforcement_scope,
                "consent_normalization_version": consent_normalization_version,
                "consent": consent,
                "user_data_hashed": user_data_hashed,
                "click_ids": click_ids,
                "session": session,
                "value_data": value_data,
                "event_source": event_source,
                "payload_expired": payload_expired,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_event_response_200_lineage_children_item_click_ids_type_0 import (
            GetEventResponse200LineageChildrenItemClickIdsType0,
        )
        from ..models.get_event_response_200_lineage_children_item_consent_type_0 import (
            GetEventResponse200LineageChildrenItemConsentType0,
        )
        from ..models.get_event_response_200_lineage_children_item_session_type_0 import (
            GetEventResponse200LineageChildrenItemSessionType0,
        )
        from ..models.get_event_response_200_lineage_children_item_user_data_hashed_type_0 import (
            GetEventResponse200LineageChildrenItemUserDataHashedType0,
        )
        from ..models.get_event_response_200_lineage_children_item_value_data_type_0 import (
            GetEventResponse200LineageChildrenItemValueDataType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        signal_tracker_id = d.pop("signal_tracker_id")

        def _parse_parent_event_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parent_event_id = _parse_parent_event_id(d.pop("parent_event_id"))

        event_name = d.pop("event_name")

        event_time = d.pop("event_time")

        action_source = d.pop("action_source")

        event_class = d.pop("event_class")

        def _parse_order_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        order_id = _parse_order_id(d.pop("order_id"))

        def _parse_value_amount(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        value_amount = _parse_value_amount(d.pop("value_amount"))

        def _parse_value_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        value_currency = _parse_value_currency(d.pop("value_currency"))

        created_at = d.pop("created_at")

        consent_basis = d.pop("consent_basis")

        measurement_class = d.pop("measurement_class")

        attribution_join = d.pop("attribution_join")

        enforcement_scope = d.pop("enforcement_scope")

        consent_normalization_version = d.pop("consent_normalization_version")

        def _parse_consent(data: object) -> GetEventResponse200LineageChildrenItemConsentType0 | list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                consent_type_0 = GetEventResponse200LineageChildrenItemConsentType0.from_dict(data)

                return consent_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                consent_type_1 = cast(list[Any], data)

                return consent_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetEventResponse200LineageChildrenItemConsentType0 | list[Any] | None, data)

        consent = _parse_consent(d.pop("consent"))

        def _parse_user_data_hashed(
            data: object,
        ) -> GetEventResponse200LineageChildrenItemUserDataHashedType0 | list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_data_hashed_type_0 = GetEventResponse200LineageChildrenItemUserDataHashedType0.from_dict(data)

                return user_data_hashed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_data_hashed_type_1 = cast(list[Any], data)

                return user_data_hashed_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetEventResponse200LineageChildrenItemUserDataHashedType0 | list[Any] | None, data)

        user_data_hashed = _parse_user_data_hashed(d.pop("user_data_hashed"))

        def _parse_click_ids(data: object) -> GetEventResponse200LineageChildrenItemClickIdsType0 | list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                click_ids_type_0 = GetEventResponse200LineageChildrenItemClickIdsType0.from_dict(data)

                return click_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                click_ids_type_1 = cast(list[Any], data)

                return click_ids_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetEventResponse200LineageChildrenItemClickIdsType0 | list[Any] | None, data)

        click_ids = _parse_click_ids(d.pop("click_ids"))

        def _parse_session(data: object) -> GetEventResponse200LineageChildrenItemSessionType0 | list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                session_type_0 = GetEventResponse200LineageChildrenItemSessionType0.from_dict(data)

                return session_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                session_type_1 = cast(list[Any], data)

                return session_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetEventResponse200LineageChildrenItemSessionType0 | list[Any] | None, data)

        session = _parse_session(d.pop("session"))

        def _parse_value_data(data: object) -> GetEventResponse200LineageChildrenItemValueDataType0 | list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_data_type_0 = GetEventResponse200LineageChildrenItemValueDataType0.from_dict(data)

                return value_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_data_type_1 = cast(list[Any], data)

                return value_data_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetEventResponse200LineageChildrenItemValueDataType0 | list[Any] | None, data)

        value_data = _parse_value_data(d.pop("value_data"))

        def _parse_event_source(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        event_source = _parse_event_source(d.pop("event_source"))

        payload_expired = d.pop("payload_expired")

        get_event_response_200_lineage_children_item = cls(
            id=id,
            signal_tracker_id=signal_tracker_id,
            parent_event_id=parent_event_id,
            event_name=event_name,
            event_time=event_time,
            action_source=action_source,
            event_class=event_class,
            order_id=order_id,
            value_amount=value_amount,
            value_currency=value_currency,
            created_at=created_at,
            consent_basis=consent_basis,
            measurement_class=measurement_class,
            attribution_join=attribution_join,
            enforcement_scope=enforcement_scope,
            consent_normalization_version=consent_normalization_version,
            consent=consent,
            user_data_hashed=user_data_hashed,
            click_ids=click_ids,
            session=session,
            value_data=value_data,
            event_source=event_source,
            payload_expired=payload_expired,
        )

        get_event_response_200_lineage_children_item.additional_properties = d
        return get_event_response_200_lineage_children_item

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
