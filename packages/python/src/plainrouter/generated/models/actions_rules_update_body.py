from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actions_rules_update_body_author_type_type_3 import ActionsRulesUpdateBodyAuthorTypeType3
    from ..models.actions_rules_update_body_current_revision_id_type_3 import (
        ActionsRulesUpdateBodyCurrentRevisionIdType3,
    )
    from ..models.actions_rules_update_body_definition_type_0 import ActionsRulesUpdateBodyDefinitionType0
    from ..models.actions_rules_update_body_definition_type_1 import ActionsRulesUpdateBodyDefinitionType1
    from ..models.actions_rules_update_body_definition_type_2 import ActionsRulesUpdateBodyDefinitionType2
    from ..models.actions_rules_update_body_window_days_type_3 import ActionsRulesUpdateBodyWindowDaysType3
    from ..models.actions_rules_update_body_window_type_3 import ActionsRulesUpdateBodyWindowType3


T = TypeVar("T", bound="ActionsRulesUpdateBody")


@_attrs_define
class ActionsRulesUpdateBody:
    """All fields are optional. platform_ad_account_id must be absent. window, window_days, author_type and
    current_revision_id must be absent or empty.

        Attributes:
            name (str | Unset):
            definition (ActionsRulesUpdateBodyDefinitionType0 | ActionsRulesUpdateBodyDefinitionType1 |
                ActionsRulesUpdateBodyDefinitionType2 | Unset):
            account_id (int | Unset): Optional integer account ID. JSON booleans return 422 with message plus field errors.
                A valid supplied ID is ignored by an account-bound key. An unbound key requires exactly one active available
                advertising account with an active connection; omission uses that account and a supplied ID must match it.
                Multiple active accounts return 422 even when account_id is supplied.
            enabled (bool | Unset):
            window (ActionsRulesUpdateBodyWindowType3 | list[Any] | Literal[''] | None | Unset):
            window_days (ActionsRulesUpdateBodyWindowDaysType3 | list[Any] | Literal[''] | None | Unset):
            author_type (ActionsRulesUpdateBodyAuthorTypeType3 | list[Any] | Literal[''] | None | Unset):
            current_revision_id (ActionsRulesUpdateBodyCurrentRevisionIdType3 | list[Any] | Literal[''] | None | Unset):
    """

    name: str | Unset = UNSET
    definition: (
        ActionsRulesUpdateBodyDefinitionType0
        | ActionsRulesUpdateBodyDefinitionType1
        | ActionsRulesUpdateBodyDefinitionType2
        | Unset
    ) = UNSET
    account_id: int | Unset = UNSET
    enabled: bool | Unset = UNSET
    window: ActionsRulesUpdateBodyWindowType3 | list[Any] | Literal[""] | None | Unset = UNSET
    window_days: ActionsRulesUpdateBodyWindowDaysType3 | list[Any] | Literal[""] | None | Unset = UNSET
    author_type: ActionsRulesUpdateBodyAuthorTypeType3 | list[Any] | Literal[""] | None | Unset = UNSET
    current_revision_id: ActionsRulesUpdateBodyCurrentRevisionIdType3 | list[Any] | Literal[""] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.actions_rules_update_body_author_type_type_3 import ActionsRulesUpdateBodyAuthorTypeType3
        from ..models.actions_rules_update_body_current_revision_id_type_3 import (
            ActionsRulesUpdateBodyCurrentRevisionIdType3,
        )
        from ..models.actions_rules_update_body_definition_type_0 import ActionsRulesUpdateBodyDefinitionType0
        from ..models.actions_rules_update_body_definition_type_1 import ActionsRulesUpdateBodyDefinitionType1
        from ..models.actions_rules_update_body_window_days_type_3 import ActionsRulesUpdateBodyWindowDaysType3
        from ..models.actions_rules_update_body_window_type_3 import ActionsRulesUpdateBodyWindowType3

        name = self.name

        definition: dict[str, Any] | Unset
        if isinstance(self.definition, Unset):
            definition = UNSET
        elif isinstance(self.definition, ActionsRulesUpdateBodyDefinitionType0):
            definition = self.definition.to_dict()
        elif isinstance(self.definition, ActionsRulesUpdateBodyDefinitionType1):
            definition = self.definition.to_dict()
        else:
            definition = self.definition.to_dict()

        account_id = self.account_id

        enabled = self.enabled

        window: dict[str, Any] | list[Any] | Literal[""] | None | Unset
        if isinstance(self.window, Unset):
            window = UNSET
        elif isinstance(self.window, list):
            window = self.window

        elif isinstance(self.window, ActionsRulesUpdateBodyWindowType3):
            window = self.window.to_dict()
        else:
            window = self.window

        window_days: dict[str, Any] | list[Any] | Literal[""] | None | Unset
        if isinstance(self.window_days, Unset):
            window_days = UNSET
        elif isinstance(self.window_days, list):
            window_days = self.window_days

        elif isinstance(self.window_days, ActionsRulesUpdateBodyWindowDaysType3):
            window_days = self.window_days.to_dict()
        else:
            window_days = self.window_days

        author_type: dict[str, Any] | list[Any] | Literal[""] | None | Unset
        if isinstance(self.author_type, Unset):
            author_type = UNSET
        elif isinstance(self.author_type, list):
            author_type = self.author_type

        elif isinstance(self.author_type, ActionsRulesUpdateBodyAuthorTypeType3):
            author_type = self.author_type.to_dict()
        else:
            author_type = self.author_type

        current_revision_id: dict[str, Any] | list[Any] | Literal[""] | None | Unset
        if isinstance(self.current_revision_id, Unset):
            current_revision_id = UNSET
        elif isinstance(self.current_revision_id, list):
            current_revision_id = self.current_revision_id

        elif isinstance(self.current_revision_id, ActionsRulesUpdateBodyCurrentRevisionIdType3):
            current_revision_id = self.current_revision_id.to_dict()
        else:
            current_revision_id = self.current_revision_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if definition is not UNSET:
            field_dict["definition"] = definition
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if window is not UNSET:
            field_dict["window"] = window
        if window_days is not UNSET:
            field_dict["window_days"] = window_days
        if author_type is not UNSET:
            field_dict["author_type"] = author_type
        if current_revision_id is not UNSET:
            field_dict["current_revision_id"] = current_revision_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.actions_rules_update_body_author_type_type_3 import ActionsRulesUpdateBodyAuthorTypeType3
        from ..models.actions_rules_update_body_current_revision_id_type_3 import (
            ActionsRulesUpdateBodyCurrentRevisionIdType3,
        )
        from ..models.actions_rules_update_body_definition_type_0 import ActionsRulesUpdateBodyDefinitionType0
        from ..models.actions_rules_update_body_definition_type_1 import ActionsRulesUpdateBodyDefinitionType1
        from ..models.actions_rules_update_body_definition_type_2 import ActionsRulesUpdateBodyDefinitionType2
        from ..models.actions_rules_update_body_window_days_type_3 import ActionsRulesUpdateBodyWindowDaysType3
        from ..models.actions_rules_update_body_window_type_3 import ActionsRulesUpdateBodyWindowType3

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_definition(
            data: object,
        ) -> (
            ActionsRulesUpdateBodyDefinitionType0
            | ActionsRulesUpdateBodyDefinitionType1
            | ActionsRulesUpdateBodyDefinitionType2
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                definition_type_0 = ActionsRulesUpdateBodyDefinitionType0.from_dict(data)

                return definition_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                definition_type_1 = ActionsRulesUpdateBodyDefinitionType1.from_dict(data)

                return definition_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            definition_type_2 = ActionsRulesUpdateBodyDefinitionType2.from_dict(data)

            return definition_type_2

        definition = _parse_definition(d.pop("definition", UNSET))

        account_id = d.pop("account_id", UNSET)

        enabled = d.pop("enabled", UNSET)

        def _parse_window(data: object) -> ActionsRulesUpdateBodyWindowType3 | list[Any] | Literal[""] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            window_type_1 = cast(Literal[""], data)
            if window_type_1 != "":
                raise ValueError(f"window_type_1 must match const '', got '{window_type_1}'")
            return window_type_1
            try:
                if not isinstance(data, list):
                    raise TypeError()
                window_type_2 = cast(list[Any], data)

                return window_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_type_3 = ActionsRulesUpdateBodyWindowType3.from_dict(data)

                return window_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionsRulesUpdateBodyWindowType3 | list[Any] | Literal[""] | None | Unset, data)

        window = _parse_window(d.pop("window", UNSET))

        def _parse_window_days(
            data: object,
        ) -> ActionsRulesUpdateBodyWindowDaysType3 | list[Any] | Literal[""] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            window_days_type_1 = cast(Literal[""], data)
            if window_days_type_1 != "":
                raise ValueError(f"window_days_type_1 must match const '', got '{window_days_type_1}'")
            return window_days_type_1
            try:
                if not isinstance(data, list):
                    raise TypeError()
                window_days_type_2 = cast(list[Any], data)

                return window_days_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_days_type_3 = ActionsRulesUpdateBodyWindowDaysType3.from_dict(data)

                return window_days_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionsRulesUpdateBodyWindowDaysType3 | list[Any] | Literal[""] | None | Unset, data)

        window_days = _parse_window_days(d.pop("window_days", UNSET))

        def _parse_author_type(
            data: object,
        ) -> ActionsRulesUpdateBodyAuthorTypeType3 | list[Any] | Literal[""] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            author_type_type_1 = cast(Literal[""], data)
            if author_type_type_1 != "":
                raise ValueError(f"author_type_type_1 must match const '', got '{author_type_type_1}'")
            return author_type_type_1
            try:
                if not isinstance(data, list):
                    raise TypeError()
                author_type_type_2 = cast(list[Any], data)

                return author_type_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_type_type_3 = ActionsRulesUpdateBodyAuthorTypeType3.from_dict(data)

                return author_type_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionsRulesUpdateBodyAuthorTypeType3 | list[Any] | Literal[""] | None | Unset, data)

        author_type = _parse_author_type(d.pop("author_type", UNSET))

        def _parse_current_revision_id(
            data: object,
        ) -> ActionsRulesUpdateBodyCurrentRevisionIdType3 | list[Any] | Literal[""] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            current_revision_id_type_1 = cast(Literal[""], data)
            if current_revision_id_type_1 != "":
                raise ValueError(f"current_revision_id_type_1 must match const '', got '{current_revision_id_type_1}'")
            return current_revision_id_type_1
            try:
                if not isinstance(data, list):
                    raise TypeError()
                current_revision_id_type_2 = cast(list[Any], data)

                return current_revision_id_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_revision_id_type_3 = ActionsRulesUpdateBodyCurrentRevisionIdType3.from_dict(data)

                return current_revision_id_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionsRulesUpdateBodyCurrentRevisionIdType3 | list[Any] | Literal[""] | None | Unset, data)

        current_revision_id = _parse_current_revision_id(d.pop("current_revision_id", UNSET))

        actions_rules_update_body = cls(
            name=name,
            definition=definition,
            account_id=account_id,
            enabled=enabled,
            window=window,
            window_days=window_days,
            author_type=author_type,
            current_revision_id=current_revision_id,
        )

        actions_rules_update_body.additional_properties = d
        return actions_rules_update_body

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
