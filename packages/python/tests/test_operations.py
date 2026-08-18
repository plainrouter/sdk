from __future__ import annotations

import datetime
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
)
from plainrouter.generated import AuthenticatedClient
from plainrouter.generated.models import (
    CreateEventBody,
    CreateEventResponse200,
    DeleteUserDataBody,
    DeleteUserDataBodyIdentifierType,
    ErrorMessage,
    ReplayDeliveriesBody,
    SendTestPurchaseBody,
    SetDestinationTestModeBody,
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

    response = create_event.sync_detailed(client=client, body=CreateEventBody(event_name="Purchase"))

    assert_error_response(response)
    assert requests[0].method == "POST"
    assert requests[0].url.path == "/api/v1/events"
    assert requests[0].read() == b'{"event_name":"Purchase"}'


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
        body=CreateEventBody(event_name="Purchase"),
    )

    assert isinstance(response.parsed, CreateEventResponse200)
    assert response.parsed.event_id == "event-123"
    assert response.parsed.duplicate is False
