from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LaunchPolicy")


@_attrs_define
class LaunchPolicy:
    """
    Attributes:
        id (str):
        workspace_id (int):
        kind (str):
        name (str):
        version (int):
        body (list[Any]):
        status (str):
        created_at (datetime.datetime | None):
        updated_at (datetime.datetime | None):
    """

    id: str
    workspace_id: int
    kind: str
    name: str
    version: int
    body: list[Any]
    status: str
    created_at: datetime.datetime | None
    updated_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workspace_id = self.workspace_id

        kind = self.kind

        name = self.name

        version = self.version

        body = self.body

        status = self.status

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workspace_id": workspace_id,
                "kind": kind,
                "name": name,
                "version": version,
                "body": body,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        workspace_id = d.pop("workspace_id")

        kind = d.pop("kind")

        name = d.pop("name")

        version = d.pop("version")

        body = cast(list[Any], d.pop("body"))

        status = d.pop("status")

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

        launch_policy = cls(
            id=id,
            workspace_id=workspace_id,
            kind=kind,
            name=name,
            version=version,
            body=body,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
        )

        launch_policy.additional_properties = d
        return launch_policy

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
