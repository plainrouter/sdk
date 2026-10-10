from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreativeIntakeTags")


@_attrs_define
class CreativeIntakeTags:
    """Optional flat map of at most 32 string tags; reserved keys count toward the cap. For a creative from an outside
    tool, set generator and generator_job, plus parent_creative for a variation. Values are stored unchanged.
    PlainRouter’s own creative tools will set these on every creative they make; intake performs no generation,
    rendering or scoring.

        Attributes:
            generator (str | Unset): Lowercase slug naming the outside tool that made the creative.
            generator_job (str | Unset): Printable characters naming the tool’s job or render; control and other non-
                printable characters are refused.
            parent_creative (str | Unset): The id returned by the creative APIs: a lowercase ULID of an existing creative in
                the same workspace that this creative varies.
    """

    generator: str | Unset = UNSET
    generator_job: str | Unset = UNSET
    parent_creative: str | Unset = UNSET
    additional_properties: dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        generator = self.generator

        generator_job = self.generator_job

        parent_creative = self.parent_creative

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if generator is not UNSET:
            field_dict["generator"] = generator
        if generator_job is not UNSET:
            field_dict["generator_job"] = generator_job
        if parent_creative is not UNSET:
            field_dict["parent_creative"] = parent_creative

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        generator = d.pop("generator", UNSET)

        generator_job = d.pop("generator_job", UNSET)

        parent_creative = d.pop("parent_creative", UNSET)

        creative_intake_tags = cls(
            generator=generator,
            generator_job=generator_job,
            parent_creative=parent_creative,
        )

        creative_intake_tags.additional_properties = d
        return creative_intake_tags

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
