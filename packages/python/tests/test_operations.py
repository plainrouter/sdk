from __future__ import annotations

import datetime
import json
from collections.abc import Callable
from typing import TypeVar

import httpx

from plainrouter import (
    create_client,
    create_event,
    delete_user_data,
    get_emq_report,
    get_event,
    get_reconciliation_report,
    list_events,
    replay_deliveries,
    send_test_purchase,
    set_destination_test_mode,
    verify_signal_ingestion,
)
from plainrouter.generated import AuthenticatedClient
from plainrouter.generated.models import (
    CreateEventBody,
    CreateEventBodyConsent,
    CreateEventBodyConsentMode,
    CreateEventBodyTcf,
    CreateEventResponse200,
    DeleteUserDataBody,
    DeleteUserDataBodyIdentifierType,
    ErrorMessage,
    Event,
    ReplayDeliveriesBody,
    SendTestPurchaseBody,
    SetDestinationTestModeBody,
    ValidationError,
    VerifySignalIngestionResponse202,
)
from plainrouter.generated.types import Response

T = TypeVar("T")


def make_client(
    handler: Callable[[httpx.Request], httpx.Response],
) -> AuthenticatedClient:
    return create_client(
        "tracker-test-secret",
        httpx_args={"transport": httpx.MockTransport(handler)},
    )


def error_handler(requests: list[httpx.Request]) -> Callable[[httpx.Request], httpx.Response]:
    def handle(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(401, json={"message": "Unauthenticated."})

    return handle


def assert_error_response(response: Response[T]) -> None:
    assert response.status_code == 401
    assert isinstance(response.parsed, ErrorMessage)
    assert response.parsed.message == "Unauthenticated."


def test_create_event_calls_generated_operation_with_body() -> None:
    requests: list[httpx.Request] = []
    client = make_client(error_handler(requests))
    consent = CreateEventBodyConsent()
    consent["analytics_storage"] = "granted"
    consent_mode = CreateEventBodyConsentMode()
    consent_mode["ad_user_data"] = "granted"
    tcf = CreateEventBodyTcf()
    tcf["string"] = (
        "COwK6gaOwK6gaFmAAAENAPCAAAAAAAAAAAAAAAAAAAAA.IFMsv_Z_G____bvQXQlf9eY1f9_z_q7t0eY1f9_z2-8v8Z9wKZ1v9t0Q"
    )

    response = create_event.sync_detailed(
        client=client,
        body=CreateEventBody(
            event_name="Purchase",
            consent_basis="consent",
            consent=consent,
            consent_mode=consent_mode,
            tcf=tcf,
        ),
    )

    assert_error_response(response)
    assert requests[0].method == "POST"
    assert requests[0].url.path == "/api/v1/events"
    assert json.loads(requests[0].read()) == {
        "event_name": "Purchase",
        "consent_basis": "consent",
        "consent": {"analytics_storage": "granted"},
        "consent_mode": {"ad_user_data": "granted"},
        "tcf": {
            "string": "COwK6gaOwK6gaFmAAAENAPCAAAAAAAAAAAAAAAAAAAAA.IFMsv_Z_G____bvQXQlf9eY1f9_z_q7t0eY1f9_z2-8v8Z9wKZ1v9t0Q"
        },
    }


def test_verify_signal_ingestion_calls_generated_operation_with_auth() -> None:
    requests: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(202, json={"event_id": "signal-verification", "duplicate": False})

    response = verify_signal_ingestion.sync_detailed(client=make_client(handle))

    assert isinstance(response.parsed, VerifySignalIngestionResponse202)
    assert response.parsed.event_id == "signal-verification"
    assert requests[0].method == "POST"
    assert requests[0].url.path == "/api/v1/verification-events"
    assert requests[0].headers["Authorization"] == "Bearer tracker-test-secret"


def test_get_event_calls_generated_operation_with_event_id() -> None:
    requests: list[httpx.Request] = []
    client = make_client(error_handler(requests))

    response = get_event.sync_detailed("event/123", client=client)

    assert_error_response(response)
    assert requests[0].method == "GET"
    assert requests[0].url.path == "/api/v1/events/event/123"
    assert requests[0].url.raw_path.endswith(b"event%2F123")


def test_list_events_calls_generated_operation_with_page_size() -> None:
    requests: list[httpx.Request] = []
    client = make_client(error_handler(requests))

    response = list_events.sync_detailed(client=client, per_page=10)

    assert_error_response(response)
    assert requests[0].method == "GET"
    assert requests[0].url.path == "/api/v1/dashboard/events"
    assert requests[0].url.params["per_page"] == "10"


def test_set_destination_test_mode_calls_generated_operation_with_body() -> None:
    requests: list[httpx.Request] = []
    client = make_client(error_handler(requests))

    response = set_destination_test_mode.sync_detailed(
        "meta/primary",
        client=client,
        body=SetDestinationTestModeBody(enabled=True, test_event_code="TEST123"),
    )

    assert_error_response(response)
    assert requests[0].method == "PATCH"
    assert requests[0].url.raw_path.endswith(b"destinations/meta%2Fprimary/test-mode")
    assert requests[0].read() == b'{"enabled":true,"test_event_code":"TEST123"}'


def test_send_test_purchase_calls_generated_operation_with_body() -> None:
    requests: list[httpx.Request] = []
    client = make_client(error_handler(requests))

    response = send_test_purchase.sync_detailed(
        "destination-1",
        client=client,
        body=SendTestPurchaseBody(value="19.95", currency="EUR", order_id="order-1"),
    )

    assert_error_response(response)
    assert requests[0].method == "POST"
    assert requests[0].url.path == "/api/v1/destinations/destination-1/test-purchase"
    assert requests[0].read() == b'{"value":"19.95","currency":"EUR","order_id":"order-1"}'


def test_send_test_purchase_distinguishes_validation_and_domain_errors() -> None:
    validation_client = make_client(
        lambda request: httpx.Response(
            422,
            json={"message": "The value field is invalid.", "errors": {"value": ["The value is invalid."]}},
        )
    )
    domain_client = make_client(lambda request: httpx.Response(422, json={"message": "Test mode is disabled."}))

    validation_response = send_test_purchase.sync_detailed("destination-1", client=validation_client)
    domain_response = send_test_purchase.sync_detailed("destination-1", client=domain_client)

    assert isinstance(validation_response.parsed, ValidationError)
    assert validation_response.parsed.errors["value"] == ["The value is invalid."]
    assert isinstance(domain_response.parsed, ErrorMessage)
    assert domain_response.parsed.message == "Test mode is disabled."


def test_replay_deliveries_calls_generated_operation_with_filters() -> None:
    requests: list[httpx.Request] = []
    client = make_client(error_handler(requests))

    response = replay_deliveries.sync_detailed(
        client=client,
        body=ReplayDeliveriesBody(delivery_ids=[10, 20], event_name="Purchase", limit=2),
    )

    assert_error_response(response)
    assert requests[0].method == "POST"
    assert requests[0].url.path == "/api/v1/deliveries/replay"
    assert requests[0].read() == b'{"delivery_ids":[10,20],"event_name":"Purchase","limit":2}'


def test_get_reconciliation_report_calls_generated_operation_with_date() -> None:
    requests: list[httpx.Request] = []
    client = make_client(error_handler(requests))

    response = get_reconciliation_report.sync_detailed(client=client, date=datetime.date(2026, 8, 18))

    assert_error_response(response)
    assert requests[0].method == "GET"
    assert requests[0].url.path == "/api/v1/reports/reconciliation"
    assert requests[0].url.params["date"] == "2026-08-18"


def test_get_emq_report_calls_generated_operation() -> None:
    requests: list[httpx.Request] = []
    client = make_client(error_handler(requests))

    response = get_emq_report.sync_detailed(client=client)

    assert_error_response(response)
    assert requests[0].method == "GET"
    assert requests[0].url.path == "/api/v1/reports/emq"


def test_delete_user_data_calls_generated_operation_with_identifier() -> None:
    requests: list[httpx.Request] = []
    client = make_client(error_handler(requests))

    response = delete_user_data.sync_detailed(
        client=client,
        body=DeleteUserDataBody(
            identifier_type=DeleteUserDataBodyIdentifierType.EMAIL,
            identifier_hash="a" * 64,
        ),
    )

    assert_error_response(response)
    assert requests[0].method == "DELETE"
    assert requests[0].url.path == "/api/v1/user-data"
    assert requests[0].read() == ('{"identifier_type":"email","identifier_hash":"' + "a" * 64 + '"}').encode()


def test_create_event_parses_a_success_response() -> None:
    def handle(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"event_id": "event-123", "duplicate": False})

    response = create_event.sync_detailed(
        client=make_client(handle),
        body=CreateEventBody(event_name="Purchase", consent_basis="consent"),
    )

    assert isinstance(response.parsed, CreateEventResponse200)
    assert response.parsed.event_id == "event-123"
    assert response.parsed.duplicate is False


def test_event_deserializes_consent_decision_fields() -> None:
    event = Event.from_dict(
        {
            "id": "event-123",
            "signal_tracker_id": "tracker-123",
            "parent_event_id": None,
            "event_name": "Purchase",
            "event_time": "2026-08-19T00:00:00+00:00",
            "action_source": "website",
            "event_class": "conversion",
            "order_id": "order-123",
            "value_amount": 1995,
            "value_currency": "EUR",
            "created_at": "2026-08-19T00:00:01+00:00",
            "consent_basis": "consent",
            "measurement_class": "advertising",
            "attribution_join": "allowed",
            "enforcement_scope": "event",
            "consent_normalization_version": "1",
            "consent": "{}",
            "user_data_hashed": "{}",
            "click_ids": "{}",
            "session": "{}",
            "value_data": "{}",
            "event_source": "https://example.test/checkout",
            "payload_expired": False,
            "deliveries": [],
        }
    )

    assert event.consent_basis == "consent"
    assert event.measurement_class == "advertising"
    assert event.attribution_join == "allowed"
    assert event.enforcement_scope == "event"
    assert event.consent_normalization_version == "1"
