from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.creative_mcp_preview_mime_type import CreativeMcpPreviewMimeType
from ..models.creative_mcp_preview_state import CreativeMcpPreviewState
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreativeMcpPreview")


@_attrs_define
class CreativeMcpPreview:
    """Missing derivatives return pending and queue a creative-queue build, including creatives created before these tools
    shipped. No image bytes are sent to the model.

        Attributes:
            id (str):
            state (CreativeMcpPreviewState):
            url (str | Unset): Ready items only, delivered in tool-result _meta.creative_previews to the MCP App. Signed R2
                derivative URL valid for at most 300 seconds; never an original or provider URL.
            mime_type (CreativeMcpPreviewMimeType | Unset):
            width (int | Unset):
            height (int | Unset):
            byte_size (int | Unset): Stored derivative at most 1048576 bytes and 4000000 pixels. SVG refused; the existing
                decode cap applies.
            expires_at (str | Unset):
    """

    id: str
    state: CreativeMcpPreviewState
    url: str | Unset = UNSET
    mime_type: CreativeMcpPreviewMimeType | Unset = UNSET
    width: int | Unset = UNSET
    height: int | Unset = UNSET
    byte_size: int | Unset = UNSET
    expires_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        state = self.state.value

        url = self.url

        mime_type: str | Unset = UNSET
        if not isinstance(self.mime_type, Unset):
            mime_type = self.mime_type.value

        width = self.width

        height = self.height

        byte_size = self.byte_size

        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "state": state,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if mime_type is not UNSET:
            field_dict["mime_type"] = mime_type
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if byte_size is not UNSET:
            field_dict["byte_size"] = byte_size
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        state = CreativeMcpPreviewState(d.pop("state"))

        url = d.pop("url", UNSET)

        _mime_type = d.pop("mime_type", UNSET)
        mime_type: CreativeMcpPreviewMimeType | Unset
        if isinstance(_mime_type, Unset):
            mime_type = UNSET
        else:
            mime_type = CreativeMcpPreviewMimeType(_mime_type)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        byte_size = d.pop("byte_size", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        creative_mcp_preview = cls(
            id=id,
            state=state,
            url=url,
            mime_type=mime_type,
            width=width,
            height=height,
            byte_size=byte_size,
            expires_at=expires_at,
        )

        creative_mcp_preview.additional_properties = d
        return creative_mcp_preview

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
