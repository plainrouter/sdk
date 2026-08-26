from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_event_body_type_0_click_ids import CreateEventBodyType0ClickIds
    from ..models.create_event_body_type_0_consent import CreateEventBodyType0Consent
    from ..models.create_event_body_type_0_consent_mode import CreateEventBodyType0ConsentMode
    from ..models.create_event_body_type_0_tcf import CreateEventBodyType0Tcf
    from ..models.create_event_body_type_0_user_data import CreateEventBodyType0UserData
    from ..models.create_event_body_type_0_value_data import CreateEventBodyType0ValueData


T = TypeVar("T", bound="CreateEventBodyType0")


@_attrs_define
class CreateEventBodyType0:
    """
    Attributes:
        event_name (str): Signal event name; maximum 100 characters.
        consent_basis (Literal['consent']): Legal basis for processing. Legitimate-interest revenue lifecycle events are
            rejected; use an authenticated server adapter.
        event_id (str | Unset): Caller-supplied idempotency key; maximum 128 characters.
        parent_event_id (str | Unset): Optional parent event id; maximum 128 characters.
        event_time (int | str | Unset): Unix timestamp or ISO-8601 date-time. Defaults to receipt time.
        event_source (str | Unset): Optional absolute source URL.
        action_source (str | Unset): Optional action source; defaults to website and is limited to 50 characters.
        visitor_id (str | Unset): Optional visitor identifier; maximum 255 characters.
        consent (CreateEventBodyType0Consent | Unset): Consent state supplied with the event.
        consent_mode (CreateEventBodyType0ConsentMode | Unset): Consent Mode v2 signal values supplied with the event.
        tcf (CreateEventBodyType0Tcf | Unset): TCF v2 data containing string and optional captured_at.
        user_data (CreateEventBodyType0UserData | Unset): Identity fields accepted by the tracker.
        click_ids (CreateEventBodyType0ClickIds | Unset): Advertising click identifiers.
        value_data (CreateEventBodyType0ValueData | Unset): Optional commerce data. Contents accepts at most 50 items
            and 16 KB serialized.
    """

    event_name: str
    consent_basis: Literal["consent"]
    event_id: str | Unset = UNSET
    parent_event_id: str | Unset = UNSET
    event_time: int | str | Unset = UNSET
    event_source: str | Unset = UNSET
    action_source: str | Unset = UNSET
    visitor_id: str | Unset = UNSET
    consent: CreateEventBodyType0Consent | Unset = UNSET
    consent_mode: CreateEventBodyType0ConsentMode | Unset = UNSET
    tcf: CreateEventBodyType0Tcf | Unset = UNSET
    user_data: CreateEventBodyType0UserData | Unset = UNSET
    click_ids: CreateEventBodyType0ClickIds | Unset = UNSET
    value_data: CreateEventBodyType0ValueData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_name = self.event_name

        consent_basis = self.consent_basis

        event_id = self.event_id

        parent_event_id = self.parent_event_id

        event_time: int | str | Unset
        if isinstance(self.event_time, Unset):
            event_time = UNSET
        else:
            event_time = self.event_time

        event_source = self.event_source

        action_source = self.action_source

        visitor_id = self.visitor_id

        consent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.consent, Unset):
            consent = self.consent.to_dict()

        consent_mode: dict[str, Any] | Unset = UNSET
        if not isinstance(self.consent_mode, Unset):
            consent_mode = self.consent_mode.to_dict()

        tcf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tcf, Unset):
            tcf = self.tcf.to_dict()

        user_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_data, Unset):
            user_data = self.user_data.to_dict()

        click_ids: dict[str, Any] | Unset = UNSET
        if not isinstance(self.click_ids, Unset):
            click_ids = self.click_ids.to_dict()

        value_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value_data, Unset):
            value_data = self.value_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_name": event_name,
                "consent_basis": consent_basis,
            }
        )
        if event_id is not UNSET:
            field_dict["event_id"] = event_id
        if parent_event_id is not UNSET:
            field_dict["parent_event_id"] = parent_event_id
        if event_time is not UNSET:
            field_dict["event_time"] = event_time
        if event_source is not UNSET:
            field_dict["event_source"] = event_source
        if action_source is not UNSET:
            field_dict["action_source"] = action_source
        if visitor_id is not UNSET:
            field_dict["visitor_id"] = visitor_id
        if consent is not UNSET:
            field_dict["consent"] = consent
        if consent_mode is not UNSET:
            field_dict["consent_mode"] = consent_mode
        if tcf is not UNSET:
            field_dict["tcf"] = tcf
        if user_data is not UNSET:
            field_dict["user_data"] = user_data
        if click_ids is not UNSET:
            field_dict["click_ids"] = click_ids
        if value_data is not UNSET:
            field_dict["value_data"] = value_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_event_body_type_0_click_ids import CreateEventBodyType0ClickIds
        from ..models.create_event_body_type_0_consent import CreateEventBodyType0Consent
        from ..models.create_event_body_type_0_consent_mode import CreateEventBodyType0ConsentMode
        from ..models.create_event_body_type_0_tcf import CreateEventBodyType0Tcf
        from ..models.create_event_body_type_0_user_data import CreateEventBodyType0UserData
        from ..models.create_event_body_type_0_value_data import CreateEventBodyType0ValueData

        d = dict(src_dict)
        event_name = d.pop("event_name")

        consent_basis = cast(Literal["consent"], d.pop("consent_basis"))
        if consent_basis != "consent":
            raise ValueError(f"consent_basis must match const 'consent', got '{consent_basis}'")

        event_id = d.pop("event_id", UNSET)

        parent_event_id = d.pop("parent_event_id", UNSET)

        def _parse_event_time(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        event_time = _parse_event_time(d.pop("event_time", UNSET))

        event_source = d.pop("event_source", UNSET)

        action_source = d.pop("action_source", UNSET)

        visitor_id = d.pop("visitor_id", UNSET)

        _consent = d.pop("consent", UNSET)
        consent: CreateEventBodyType0Consent | Unset
        if isinstance(_consent, Unset):
            consent = UNSET
        else:
            consent = CreateEventBodyType0Consent.from_dict(_consent)

        _consent_mode = d.pop("consent_mode", UNSET)
        consent_mode: CreateEventBodyType0ConsentMode | Unset
        if isinstance(_consent_mode, Unset):
            consent_mode = UNSET
        else:
            consent_mode = CreateEventBodyType0ConsentMode.from_dict(_consent_mode)

        _tcf = d.pop("tcf", UNSET)
        tcf: CreateEventBodyType0Tcf | Unset
        if isinstance(_tcf, Unset):
            tcf = UNSET
        else:
            tcf = CreateEventBodyType0Tcf.from_dict(_tcf)

        _user_data = d.pop("user_data", UNSET)
        user_data: CreateEventBodyType0UserData | Unset
        if isinstance(_user_data, Unset):
            user_data = UNSET
        else:
            user_data = CreateEventBodyType0UserData.from_dict(_user_data)

        _click_ids = d.pop("click_ids", UNSET)
        click_ids: CreateEventBodyType0ClickIds | Unset
        if isinstance(_click_ids, Unset):
            click_ids = UNSET
        else:
            click_ids = CreateEventBodyType0ClickIds.from_dict(_click_ids)

        _value_data = d.pop("value_data", UNSET)
        value_data: CreateEventBodyType0ValueData | Unset
        if isinstance(_value_data, Unset):
            value_data = UNSET
        else:
            value_data = CreateEventBodyType0ValueData.from_dict(_value_data)

        create_event_body_type_0 = cls(
            event_name=event_name,
            consent_basis=consent_basis,
            event_id=event_id,
            parent_event_id=parent_event_id,
            event_time=event_time,
            event_source=event_source,
            action_source=action_source,
            visitor_id=visitor_id,
            consent=consent,
            consent_mode=consent_mode,
            tcf=tcf,
            user_data=user_data,
            click_ids=click_ids,
            value_data=value_data,
        )

        create_event_body_type_0.additional_properties = d
        return create_event_body_type_0

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
