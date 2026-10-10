from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ad_test_list_read_observed_conversion_events_item import AdTestListReadObservedConversionEventsItem
    from ..models.ad_test_list_read_tests import AdTestListReadTests


T = TypeVar("T", bound="AdTestListRead")


@_attrs_define
class AdTestListRead:
    """
    Attributes:
        tests (AdTestListReadTests):
        observed_conversion_events_available (bool):
        observed_conversion_events (list[AdTestListReadObservedConversionEventsItem]):
    """

    tests: AdTestListReadTests
    observed_conversion_events_available: bool
    observed_conversion_events: list[AdTestListReadObservedConversionEventsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tests = self.tests.to_dict()

        observed_conversion_events_available = self.observed_conversion_events_available

        observed_conversion_events = []
        for observed_conversion_events_item_data in self.observed_conversion_events:
            observed_conversion_events_item = observed_conversion_events_item_data.to_dict()
            observed_conversion_events.append(observed_conversion_events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tests": tests,
                "observed_conversion_events_available": observed_conversion_events_available,
                "observed_conversion_events": observed_conversion_events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ad_test_list_read_observed_conversion_events_item import (
            AdTestListReadObservedConversionEventsItem,
        )
        from ..models.ad_test_list_read_tests import AdTestListReadTests

        d = dict(src_dict)
        tests = AdTestListReadTests.from_dict(d.pop("tests"))

        observed_conversion_events_available = d.pop("observed_conversion_events_available")

        observed_conversion_events = []
        _observed_conversion_events = d.pop("observed_conversion_events")
        for observed_conversion_events_item_data in _observed_conversion_events:
            observed_conversion_events_item = AdTestListReadObservedConversionEventsItem.from_dict(
                observed_conversion_events_item_data
            )

            observed_conversion_events.append(observed_conversion_events_item)

        ad_test_list_read = cls(
            tests=tests,
            observed_conversion_events_available=observed_conversion_events_available,
            observed_conversion_events=observed_conversion_events,
        )

        ad_test_list_read.additional_properties = d
        return ad_test_list_read

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
