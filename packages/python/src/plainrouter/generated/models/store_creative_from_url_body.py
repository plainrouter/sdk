from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.store_creative_from_url_body_tags import StoreCreativeFromUrlBodyTags


T = TypeVar("T", bound="StoreCreativeFromUrlBody")


@_attrs_define
class StoreCreativeFromUrlBody:
    """
    Attributes:
        url (str): Vetted HTTPS URL to fetch; private addresses and unsafe redirects are refused.
        tags (StoreCreativeFromUrlBodyTags | Unset): Optional flat map of at most 32 string tags; reserved keys count
            toward the cap. For a creative from an outside tool, set generator and generator_job, plus parent_creative for a
            variation. Values are stored unchanged. PlainRouter’s own creative tools will set these on every creative they
            make; intake performs no generation, rendering or scoring.
        source_ref (None | str | Unset):
    """

    url: str
    tags: StoreCreativeFromUrlBodyTags | Unset = UNSET
    source_ref: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        source_ref: None | str | Unset
        if isinstance(self.source_ref, Unset):
            source_ref = UNSET
        else:
            source_ref = self.source_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if source_ref is not UNSET:
            field_dict["source_ref"] = source_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.store_creative_from_url_body_tags import StoreCreativeFromUrlBodyTags

        d = dict(src_dict)
        url = d.pop("url")

        _tags = d.pop("tags", UNSET)
        tags: StoreCreativeFromUrlBodyTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = StoreCreativeFromUrlBodyTags.from_dict(_tags)

        def _parse_source_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_ref = _parse_source_ref(d.pop("source_ref", UNSET))

        store_creative_from_url_body = cls(
            url=url,
            tags=tags,
            source_ref=source_ref,
        )

        store_creative_from_url_body.additional_properties = d
        return store_creative_from_url_body

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
