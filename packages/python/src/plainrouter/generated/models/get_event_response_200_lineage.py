from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_event_response_200_lineage_children_item import GetEventResponse200LineageChildrenItem
    from ..models.get_event_response_200_lineage_parent_type_0 import GetEventResponse200LineageParentType0


T = TypeVar("T", bound="GetEventResponse200Lineage")


@_attrs_define
class GetEventResponse200Lineage:
    """
    Attributes:
        parent (GetEventResponse200LineageParentType0 | None):
        children (list[GetEventResponse200LineageChildrenItem]):
    """

    parent: GetEventResponse200LineageParentType0 | None
    children: list[GetEventResponse200LineageChildrenItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_event_response_200_lineage_parent_type_0 import GetEventResponse200LineageParentType0

        parent: dict[str, Any] | None
        if isinstance(self.parent, GetEventResponse200LineageParentType0):
            parent = self.parent.to_dict()
        else:
            parent = self.parent

        children = []
        for children_item_data in self.children:
            children_item = children_item_data.to_dict()
            children.append(children_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent": parent,
                "children": children,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_event_response_200_lineage_children_item import GetEventResponse200LineageChildrenItem
        from ..models.get_event_response_200_lineage_parent_type_0 import GetEventResponse200LineageParentType0

        d = dict(src_dict)

        def _parse_parent(data: object) -> GetEventResponse200LineageParentType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_type_0 = GetEventResponse200LineageParentType0.from_dict(data)

                return parent_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetEventResponse200LineageParentType0 | None, data)

        parent = _parse_parent(d.pop("parent"))

        children = []
        _children = d.pop("children")
        for children_item_data in _children:
            children_item = GetEventResponse200LineageChildrenItem.from_dict(children_item_data)

            children.append(children_item)

        get_event_response_200_lineage = cls(
            parent=parent,
            children=children,
        )

        get_event_response_200_lineage.additional_properties = d
        return get_event_response_200_lineage

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
