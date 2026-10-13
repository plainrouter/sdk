from __future__ import annotations

import httpx
import pytest

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


@pytest.mark.parametrize("accept", [None, "text/html", "*/*"])
async def test_json_accept_default_and_override_sync_and_async(accept: str | None) -> None:
    observed: list[str] = []

    def handle(request: httpx.Request) -> httpx.Response:
        observed.append(request.headers["Accept"])
        return httpx.Response(401, json={"message": "Unauthenticated."})

    client = create_client("test", httpx_args={"transport": httpx.MockTransport(handle)})
    configured = client.with_headers({"accept": accept}) if accept is not None else client
    with configured:
        list_events.sync_detailed(client=configured)
    async with configured:
        await list_events.asyncio_detailed(client=configured)
    assert observed == [accept or "application/json"] * 2


@pytest.mark.parametrize("status", [300, 301, 302, 303, 304, 307, 308, 399])
@pytest.mark.parametrize("follow", [False, True])
async def test_redirect_raises_before_parsing_or_following_sync_and_async(status: int, follow: bool) -> None:
    observed: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        observed.append(request)
        return httpx.Response(status, text="<html>Redirect</html>", headers={"Location": "/html"})

    client = create_client("test", follow_redirects=follow, httpx_args={"transport": httpx.MockTransport(handle)})
    with client:
        with pytest.raises(httpx.HTTPStatusError) as sync_error:
            list_events.sync_detailed(client=client)
    async with client:
        with pytest.raises(httpx.HTTPStatusError) as async_error:
            await list_events.asyncio_detailed(client=client)
    for error in (sync_error.value, async_error.value):
        assert error.response.status_code == status
        assert error.response.headers["Location"] == "/html"
    assert len(observed) == 2
