from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.launch_creatives_index_response_200_creatives_data_item_status import (
    LaunchCreativesIndexResponse200CreativesDataItemStatus,
)
from ..models.launch_creatives_index_response_200_creatives_data_item_type import (
    LaunchCreativesIndexResponse200CreativesDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.launch_creatives_index_response_200_creatives_data_item_tags_type_0 import (
        LaunchCreativesIndexResponse200CreativesDataItemTagsType0,
    )


T = TypeVar("T", bound="LaunchCreativesIndexResponse200CreativesDataItem")


@_attrs_define
class LaunchCreativesIndexResponse200CreativesDataItem:
    """
    Attributes:
        id (str):
        fingerprint (str):
        type_ (LaunchCreativesIndexResponse200CreativesDataItemType):
        mime_type (str):
        byte_size (int):
        width (int | None):
        height (int | None):
        aspect_ratio (float | None):
        duration_ms (int | None):
        source_ref (None | str):
        tags (LaunchCreativesIndexResponse200CreativesDataItemTagsType0 | list[str]): Stored tags, including provenance
            when supplied. An empty map is returned as an empty array. Existing creatives keep their original tags.
        status (LaunchCreativesIndexResponse200CreativesDataItemStatus):
        created_at (None | str):
        updated_at (None | str):
        original_filename (None | str | Unset):
    """

    id: str
    fingerprint: str
    type_: LaunchCreativesIndexResponse200CreativesDataItemType
    mime_type: str
    byte_size: int
    width: int | None
    height: int | None
    aspect_ratio: float | None
    duration_ms: int | None
    source_ref: None | str
    tags: LaunchCreativesIndexResponse200CreativesDataItemTagsType0 | list[str]
    status: LaunchCreativesIndexResponse200CreativesDataItemStatus
    created_at: None | str
    updated_at: None | str
    original_filename: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.launch_creatives_index_response_200_creatives_data_item_tags_type_0 import (
            LaunchCreativesIndexResponse200CreativesDataItemTagsType0,
        )

        id = self.id

        fingerprint = self.fingerprint

        type_ = self.type_.value

        mime_type = self.mime_type

        byte_size = self.byte_size

        width: int | None
        width = self.width

        height: int | None
        height = self.height

        aspect_ratio: float | None
        aspect_ratio = self.aspect_ratio

        duration_ms: int | None
        duration_ms = self.duration_ms

        source_ref: None | str
        source_ref = self.source_ref

        tags: dict[str, Any] | list[str]
        if isinstance(self.tags, LaunchCreativesIndexResponse200CreativesDataItemTagsType0):
            tags = self.tags.to_dict()
        else:
            tags = self.tags

        status = self.status.value

        created_at: None | str
        created_at = self.created_at

        updated_at: None | str
        updated_at = self.updated_at

        original_filename: None | str | Unset
        if isinstance(self.original_filename, Unset):
            original_filename = UNSET
        else:
            original_filename = self.original_filename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fingerprint": fingerprint,
                "type": type_,
                "mime_type": mime_type,
                "byte_size": byte_size,
                "width": width,
                "height": height,
                "aspect_ratio": aspect_ratio,
                "duration_ms": duration_ms,
                "source_ref": source_ref,
                "tags": tags,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if original_filename is not UNSET:
            field_dict["original_filename"] = original_filename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.launch_creatives_index_response_200_creatives_data_item_tags_type_0 import (
            LaunchCreativesIndexResponse200CreativesDataItemTagsType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        fingerprint = d.pop("fingerprint")

        type_ = LaunchCreativesIndexResponse200CreativesDataItemType(d.pop("type"))

        mime_type = d.pop("mime_type")

        byte_size = d.pop("byte_size")

        def _parse_width(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        width = _parse_width(d.pop("width"))

        def _parse_height(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        height = _parse_height(d.pop("height"))

        def _parse_aspect_ratio(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        aspect_ratio = _parse_aspect_ratio(d.pop("aspect_ratio"))

        def _parse_duration_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms"))

        def _parse_source_ref(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_ref = _parse_source_ref(d.pop("source_ref"))

        def _parse_tags(data: object) -> LaunchCreativesIndexResponse200CreativesDataItemTagsType0 | list[str]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tags_type_0 = LaunchCreativesIndexResponse200CreativesDataItemTagsType0.from_dict(data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            tags_type_1 = cast(list[str], data)

            return tags_type_1

        tags = _parse_tags(d.pop("tags"))

        status = LaunchCreativesIndexResponse200CreativesDataItemStatus(d.pop("status"))

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("created_at"))

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        def _parse_original_filename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        original_filename = _parse_original_filename(d.pop("original_filename", UNSET))

        launch_creatives_index_response_200_creatives_data_item = cls(
            id=id,
            fingerprint=fingerprint,
            type_=type_,
            mime_type=mime_type,
            byte_size=byte_size,
            width=width,
            height=height,
            aspect_ratio=aspect_ratio,
            duration_ms=duration_ms,
            source_ref=source_ref,
            tags=tags,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            original_filename=original_filename,
        )

        launch_creatives_index_response_200_creatives_data_item.additional_properties = d
        return launch_creatives_index_response_200_creatives_data_item

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
