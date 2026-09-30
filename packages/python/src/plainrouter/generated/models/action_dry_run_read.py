from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.action_dry_run_read_dry_run import ActionDryRunReadDryRun


T = TypeVar("T", bound="ActionDryRunRead")


@_attrs_define
class ActionDryRunRead:
    """
    Attributes:
        dry_run (ActionDryRunReadDryRun):
    """

    dry_run: ActionDryRunReadDryRun
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dry_run = self.dry_run.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dry_run": dry_run,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_dry_run_read_dry_run import ActionDryRunReadDryRun

        d = dict(src_dict)
        dry_run = ActionDryRunReadDryRun.from_dict(d.pop("dry_run"))

        action_dry_run_read = cls(
            dry_run=dry_run,
        )

        action_dry_run_read.additional_properties = d
        return action_dry_run_read

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
