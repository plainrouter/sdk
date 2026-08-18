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


async def test_async_client_injects_signal_tracker_bearer_token() -> None:
    observed: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        observed.append(request)
        return httpx.Response(401, json={"message": "Unauthenticated."})

    client = create_client("async-secret", httpx_args={"transport": httpx.MockTransport(handle)})
    await list_events.asyncio_detailed(client=client)

    assert observed[0].headers["Authorization"] == "Bearer async-secret"
