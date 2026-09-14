from __future__ import annotations

import json
from collections.abc import Callable
from typing import Any, cast

import httpx
import pytest

from plainrouter import create_client, create_event
from plainrouter.generated.models import (
    CreateEventBodyType0,
    CreateEventBodyType0Consent,
    CreateEventBodyType0UserData,
    CreateEventResponse200,
    CreateEventResponse202,
    IngestionWarningCode,
)
from plainrouter.generated.types import UNSET, Unset
from plainrouter.validation import validate_create_event_body

VALID_CAPTURED_AT = "2026-08-19T12:34:56.123456+02:00"
VALID_CAPTURED_AT_Z = "2026-08-19T10:34:56Z"


def event_body(
    *,
    visitor_id: str | None | object = None,
    user_data: dict[str, Any] | None | object = None,
    captured_at: str | None | object = None,
    include_visitor_id: bool = False,
    include_user_data: bool = False,
    include_captured_at: bool = False,
) -> dict[str, Any]:
    body: dict[str, Any] = {
        "event_name": "Purchase",
        "consent_basis": "consent",
    }
    if include_visitor_id:
        body["visitor_id"] = visitor_id
    if include_user_data:
        body["user_data"] = user_data
    if include_captured_at:
        body["consent"] = {"captured_at": captured_at}
    return body


def generated_event_body(
    *,
    visitor_id: str | None | Unset = UNSET,
    user_data: dict[str, Any] | None | Unset = UNSET,
    captured_at: str | None | Unset = UNSET,
    include_visitor_id: bool = False,
    include_user_data: bool = False,
    include_captured_at: bool = False,
) -> CreateEventBodyType0:
    kwargs: dict[str, Any] = {}
    if include_visitor_id:
        kwargs["visitor_id"] = visitor_id
    if include_user_data:
        if user_data is None or isinstance(user_data, Unset):
            kwargs["user_data"] = user_data
        else:
            user_data_model = CreateEventBodyType0UserData()
            user_data_model.additional_properties.update(user_data)
            kwargs["user_data"] = user_data_model
    if include_captured_at:
        consent = CreateEventBodyType0Consent()
        consent["captured_at"] = captured_at
        kwargs["consent"] = consent

    return CreateEventBodyType0(event_name="Purchase", consent_basis="consent", **kwargs)


def make_client(
    handler: Callable[[httpx.Request], httpx.Response],
) -> Any:
    return create_client(
        "tracker-test-secret",
        base_url="https://example.test/api/v1",
        httpx_args={"transport": httpx.MockTransport(handler)},
    )


def assert_no_http_call_before_validation(
    body: CreateEventBodyType0,
    expected_reason: str,
) -> None:
    requests: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(202, json={"event_id": "unexpected", "duplicate": False, "warnings": []})

    with pytest.raises(ValueError, match=rf"consent\.captured_at.*{expected_reason}"):
        create_event.sync_detailed(client=make_client(handle), body=body)

    assert requests == []


def test_visitor_id_without_captured_at_fails_before_transport_call() -> None:
    assert_no_http_call_before_validation(
        generated_event_body(visitor_id="visitor-123", include_visitor_id=True),
        "(required|missing)",
    )


def test_user_data_with_space_separator_fails_before_transport_call() -> None:
    assert_no_http_call_before_validation(
        generated_event_body(
            user_data={"em": "hashed-email"},
            captured_at="2026-08-19 12:34:56+02:00",
            include_user_data=True,
            include_captured_at=True,
        ),
        "(invalid|format|ISO)",
    )


def test_valid_captured_at_is_sent_byte_identical_to_input() -> None:
    requests: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(
            202,
            json={"event_id": "event-123", "duplicate": False, "warnings": []},
        )

    response = create_event.sync_detailed(
        client=make_client(handle),
        body=generated_event_body(
            visitor_id="visitor-123",
            captured_at=VALID_CAPTURED_AT,
            include_visitor_id=True,
            include_captured_at=True,
        ),
    )

    assert response.status_code == 202
    assert requests
    raw_body = requests[0].read()
    assert f'"captured_at":"{VALID_CAPTURED_AT}"'.encode() in raw_body
    assert json.loads(raw_body)["consent"]["captured_at"] == VALID_CAPTURED_AT


def test_event_without_identity_does_not_require_captured_at() -> None:
    requests: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(
            202,
            json={"event_id": "event-123", "duplicate": False, "warnings": []},
        )

    response = create_event.sync_detailed(
        client=make_client(handle),
        body=generated_event_body(),
    )

    assert response.status_code == 202
    assert response.parsed is not None
    assert requests


def test_explicit_null_identity_fields_do_not_require_captured_at() -> None:
    requests: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(
            202,
            json={"event_id": "event-123", "duplicate": False, "warnings": []},
        )

    response = create_event.sync_detailed(
        client=make_client(handle),
        body=cast(
            CreateEventBodyType0,
            event_body(
                visitor_id=None,
                user_data=None,
                include_visitor_id=True,
                include_user_data=True,
            ),
        ),
    )

    assert response.status_code == 202
    assert response.parsed is not None
    assert requests


def test_202_warning_is_typed_and_does_not_throw() -> None:
    warning = {
        "code": "consent_captured_at_invalid",
        "field": "consent.captured_at",
        "message": "Consent capture time must be ISO-8601.",
    }

    response = create_event.sync_detailed(
        client=make_client(
            lambda _request: httpx.Response(
                202,
                json={"event_id": "event-warning", "duplicate": False, "warnings": [warning]},
            )
        ),
        body=generated_event_body(),
    )

    assert isinstance(response.parsed, CreateEventResponse202)
    assert response.parsed.warnings
    parsed_warning = response.parsed.warnings[0]
    assert parsed_warning.code == IngestionWarningCode.CONSENT_CAPTURED_AT_INVALID
    assert isinstance(parsed_warning.code, IngestionWarningCode)
    assert parsed_warning.field == "consent.captured_at"
    assert parsed_warning.message == warning["message"]


def test_200_duplicate_has_no_warnings_and_does_not_throw() -> None:
    response = create_event.sync_detailed(
        client=make_client(
            lambda _request: httpx.Response(
                200,
                json={"event_id": "event-duplicate", "duplicate": True},
            )
        ),
        body=generated_event_body(),
    )

    assert isinstance(response.parsed, CreateEventResponse200)
    assert response.parsed.to_dict() == {"event_id": "event-duplicate", "duplicate": True}
    assert "warnings" not in response.parsed.to_dict()


@pytest.mark.parametrize(
    ("label", "captured_at", "valid"),
    [
        ("T with numeric offset", VALID_CAPTURED_AT, True),
        ("T with Z offset", VALID_CAPTURED_AT_Z, True),
        ("space separator", "2026-08-19 12:34:56+02:00", False),
        ("missing offset", "2026-08-19T12:34:56", False),
        ("empty", "", False),
        ("null", None, False),
    ],
)
def test_validator_matches_server_captured_at_fixtures(
    label: str,
    captured_at: str | None,
    valid: bool,
) -> None:
    body = event_body(
        visitor_id="visitor-123",
        captured_at=captured_at,
        include_visitor_id=True,
        include_captured_at=True,
    )

    if valid:
        validate_create_event_body(body)
    else:
        with pytest.raises(ValueError, match="consent\\.captured_at"):
            validate_create_event_body(body)
