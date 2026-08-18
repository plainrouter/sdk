from __future__ import annotations

import httpx

from plainrouter import create_client, list_events


def test_sync_client_injects_signal_tracker_bearer_token() -> None:
    observed: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        observed.append(request)
        return httpx.Response(401, json={"message": "Unauthenticated."})

    client = create_client("sync-secret", httpx_args={"transport": httpx.MockTransport(handle)})
    list_events.sync_detailed(client=client)

    assert observed[0].headers["Authorization"] == "Bearer sync-secret"


def test_client_uses_a_30_second_default_timeout() -> None:
    client = create_client(
        "timeout-secret", httpx_args={"transport": httpx.MockTransport(lambda request: httpx.Response(200))}
    )

    timeout = client.get_httpx_client().timeout

    assert timeout.connect == 30.0
    assert timeout.read == 30.0
    assert timeout.write == 30.0
    assert timeout.pool == 30.0


def test_client_accepts_an_explicit_no_timeout_configuration() -> None:
    client = create_client(
        "timeout-secret",
        timeout=httpx.Timeout(None),
        httpx_args={"transport": httpx.MockTransport(lambda request: httpx.Response(200))},
    )

    timeout = client.get_httpx_client().timeout

    assert timeout.connect is None
    assert timeout.read is None
    assert timeout.write is None
    assert timeout.pool is None


async def test_async_client_injects_signal_tracker_bearer_token() -> None:
    observed: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        observed.append(request)
        return httpx.Response(401, json={"message": "Unauthenticated."})

    client = create_client("async-secret", httpx_args={"transport": httpx.MockTransport(handle)})
    await list_events.asyncio_detailed(client=client)

    assert observed[0].headers["Authorization"] == "Bearer async-secret"
