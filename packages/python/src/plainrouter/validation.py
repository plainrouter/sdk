from __future__ import annotations

import re
from collections.abc import Mapping
from datetime import datetime

from .generated.types import UNSET, Unset

# Keep this literal identical to app/Domains/Signals/Data/ConsentDecision.php::CAPTURED_AT_PATTERN.
CAPTURED_AT_PATTERN = r"/\A(?<datetime>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})(?:\.(?<fraction>\d{1,6}))?(?<offset>Z|[+-](?:[01]\d|2[0-3]):[0-5]\d)\z/"
_CAPTURED_AT_REGEX = re.compile(
    CAPTURED_AT_PATTERN[1:-1]
    .replace(r"\A", "^")
    .replace(r"\z", r"\Z")
    .replace("(?<datetime>", "(?P<datetime>")
    .replace("(?<fraction>", "(?P<fraction>")
    .replace("(?<offset>", "(?P<offset>")
)


class CreateEventValidationError(ValueError):
    """Raised when an identity-bearing event omits or misformats its capture time."""


def _field_value(body: object, name: str) -> object:
    if isinstance(body, Mapping):
        return body.get(name, UNSET)

    return getattr(body, name, UNSET)


def _captured_at_value(consent: object) -> object:
    if isinstance(consent, Mapping):
        return consent.get("captured_at", UNSET)
    if consent is None or isinstance(consent, Unset):
        return UNSET

    to_dict = getattr(consent, "to_dict", None)
    if callable(to_dict):
        return to_dict().get("captured_at", UNSET)

    return getattr(consent, "captured_at", UNSET)


def _has_valid_captured_at_format(value: object) -> bool:
    if not isinstance(value, str):
        return False

    match = _CAPTURED_AT_REGEX.fullmatch(value)
    if match is None:
        return False

    fraction = match.group("fraction") or ""
    offset = match.group("offset")
    normalized_offset = "+00:00" if offset == "Z" else offset

    try:
        datetime.strptime(
            f"{match.group('datetime')}.{fraction.ljust(6, '0')}{normalized_offset}",
            "%Y-%m-%dT%H:%M:%S.%f%z",
        )
    except ValueError:
        return False

    return True


def validate_create_event_body(body: object) -> None:
    """Validate the identity/capture-time relationship before POST /events."""

    visitor_id = _field_value(body, "visitor_id")
    user_data = _field_value(body, "user_data")
    identity_present = not isinstance(visitor_id, Unset) and visitor_id is not None
    identity_present = identity_present or (not isinstance(user_data, Unset) and user_data is not None)

    if not identity_present:
        return

    captured_at = _captured_at_value(_field_value(body, "consent"))
    if isinstance(captured_at, Unset) or captured_at is None:
        raise CreateEventValidationError(
            "consent.captured_at is required when visitor_id or user_data is present (missing)."
        )

    if not _has_valid_captured_at_format(captured_at):
        raise CreateEventValidationError(
            "consent.captured_at has invalid format; expected the strict ISO-8601 capture time grammar (invalid format)."
        )
