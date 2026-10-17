from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from io import BytesIO
from threading import Thread
from typing import cast

import httpx
import pytest

from plainrouter import Client, create_client, list_events
from plainrouter.generated.api.action_proposal_api import actions_api_propose
from plainrouter.generated.api.agent_context import agent_context as agent_context_api
from plainrouter.generated.api.creative import launch_creatives_index
from plainrouter.generated.api.draft_batch_file_import import launcher_file_import
from plainrouter.generated.models import (
    ActionProposalInput,
    ActionProposalInputTargetSource,
    ApiRouteNotFound,
    DraftBatchFileImportRequest,
    DraftBatchMode,
)
from plainrouter.generated.types import File


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
    bodies: list[bytes] = []

    def handle(request: httpx.Request) -> httpx.Response:
        observed.append(request)
        bodies.append(request.read())
        return httpx.Response(401, json={"message": "Unauthenticated."})

    client = create_client(
        "async-secret",
        base_url="https://example.test/api/v1",
        httpx_args={"transport": httpx.MockTransport(handle)},
    )
    await list_events.asyncio_detailed(client=client)

    assert observed[0].headers["Authorization"] == "Bearer async-secret"
    assert len(observed) == 1

    def proposal(limit: int) -> ActionProposalInput:
        return ActionProposalInput(
            actions=[],
            rationale="Read the proposal page.",
            idempotency_key="integer-test",
            evidence=[],
            target_source=ActionProposalInputTargetSource.HUMAN_SUPPLIED,
            limit=limit,
        )

    def import_body(account_id: int) -> DraftBatchFileImportRequest:
        return DraftBatchFileImportRequest(
            file=File(payload=BytesIO(b"image")),
            source_adset_id="source-adset",
            source_ad_id="source-ad",
            mode=DraftBatchMode.ADD_TO_ADSET,
            account_id=account_id,
        )

    with pytest.raises(TypeError, match="limit"):
        actions_api_propose.sync_detailed(1, client=client, body=proposal(True))
    with pytest.raises(TypeError, match="limit"):
        await actions_api_propose.asyncio_detailed(1, client=client, body=proposal(True))
    with pytest.raises(TypeError, match="workspace"):
        actions_api_propose.sync_detailed(True, client=client, body=proposal(1))
    with pytest.raises(TypeError, match="page"):
        launch_creatives_index.sync_detailed(1, client=client, page=True)
    with pytest.raises(TypeError, match="page"):
        await launch_creatives_index.asyncio_detailed(1, client=client, page=True)
    with pytest.raises(TypeError, match="account_id"):
        launcher_file_import.sync_detailed(client=client, body=import_body(True))
    with pytest.raises(TypeError, match="account_id"):
        await launcher_file_import.asyncio_detailed(client=client, body=import_body(True))
    with pytest.raises(TypeError, match="limit"):
        client.get_httpx_client().post(
            "/agent/workspaces/1/actions", json={"limit": True}, headers={"Content-Type": "text/plain"}
        )
    with pytest.raises(TypeError, match="limit"):
        client.get_httpx_client().post(
            "/agent/workspaces/1/actions", json={"limit": True}, headers={"Content-Type": "multipart/form-data"}
        )
    assert len(observed) == 1

    for value in (1, cast(int, "12")):
        actions_api_propose.sync_detailed(1, client=client, body=proposal(value))
        await actions_api_propose.asyncio_detailed(1, client=client, body=proposal(value))
    for value in (1, cast(int, "12")):
        launcher_file_import.sync_detailed(client=client, body=import_body(value))
        await launcher_file_import.asyncio_detailed(client=client, body=import_body(value))

    assert len(observed) == 9
    assert [json.loads(body)["limit"] for body in bodies[1:3]] == [1, 1]
    assert [json.loads(body)["limit"] for body in bodies[3:5]] == ["12", "12"]
    assert all(b'name="account_id"\r\nContent-Type: text/plain\r\n\r\n1\r\n' in body for body in bodies[5:7])
    assert all(b'name="account_id"\r\nContent-Type: text/plain\r\n\r\n12\r\n' in body for body in bodies[7:9])
    client.get_httpx_client().close()
    await client.get_async_httpx_client().aclose()


@pytest.mark.parametrize("name", ["Accept", "ACCEPT", "accept"])
@pytest.mark.parametrize("accept", [None, "text/html", "*/*"])
async def test_json_accept_default_and_override_sync_and_async(name: str, accept: str | None) -> None:
    observed: list[str] = []

    def handle(request: httpx.Request) -> httpx.Response:
        observed.append(request.headers["Accept"])
        return httpx.Response(401, json={"message": "Unauthenticated."})

    client = create_client("test", httpx_args={"transport": httpx.MockTransport(handle)})
    configured = client.with_headers({name: accept}) if accept is not None else client
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


@pytest.mark.parametrize(
    "name,injected,anonymous,accept",
    [
        ("Accept", False, False, "text/csv"),
        ("ACCEPT", False, False, "text/csv"),
        ("accept", False, False, "text/csv"),
        ("dual", False, False, "text/csv"),
        ("dual", False, True, "text/csv"),
        ("dual", True, False, "text/csv"),
        ("dual", True, True, "text/csv"),
        ("dual", True, False, "*/*"),
        ("dual", True, True, "*/*"),
    ],
)
async def test_repeated_header_overrides_and_derivation_do_not_duplicate_headers(
    name: str, injected: bool, anonymous: bool, accept: str
) -> None:
    requests: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(401, json={"message": "Unauthenticated."})

    transport = httpx.MockTransport(handle)
    client = (
        Client(base_url="https://example.test", httpx_args={"transport": transport})
        if anonymous
        else create_client("derived-test", base_url="https://example.test", httpx_args={"transport": transport})
    )
    if injected:
        headers = {"Accept": "*/*", "Authorization": "Bearer derived-test"}
        client.set_httpx_client(httpx.Client(base_url="https://example.test", headers=headers, transport=transport))
        client.set_async_httpx_client(
            httpx.AsyncClient(base_url="https://example.test", headers=headers, transport=transport)
        )
    list_events.sync_detailed(client=client)
    await list_events.asyncio_detailed(client=client)
    if name == "dual":
        derived = client.with_headers(
            {
                "accept": "text/html",
                "Accept": accept,
                "authorization": "Bearer ignored",
                "Authorization": "Bearer derived-test",
            }
        )
    else:
        derived = client.with_headers({name: "text/html"}).with_headers({name.swapcase(): accept})
    if name == "dual":
        list_events.sync_detailed(client=client)
        await list_events.asyncio_detailed(client=client)
    variants = [derived, derived.with_timeout(httpx.Timeout(10)), derived.with_cookies({"test": "cookie"})]
    for variant in variants:
        list_events.sync_detailed(client=variant)
        await list_events.asyncio_detailed(client=variant)
    assert len(requests) == (10 if name == "dual" else 8)
    for request in requests[:2]:
        assert [value for key, value in request.headers.raw if key.lower() == b"accept"] == [b"application/json"]
    for request in requests[2:]:
        assert [value for key, value in request.headers.raw if key.lower() == b"accept"] == [accept.encode()]
        assert [value for key, value in request.headers.raw if key.lower() == b"authorization"] == [
            b"Bearer derived-test"
        ]
    for variant in [client, *variants]:
        variant.get_httpx_client().close()
        await variant.get_async_httpx_client().aclose()


@pytest.mark.parametrize("accept", [None, "*/*", "application/vnd.x+json"])
async def test_injected_clients_apply_json_default_and_preserve_custom_accept(accept: str | None) -> None:
    requests: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(401, json={"message": "Unauthenticated."})

    headers = {} if accept is None else {"Accept": accept}
    client = create_client("injected-test")
    client.set_httpx_client(
        httpx.Client(base_url="https://example.test", headers=headers, transport=httpx.MockTransport(handle))
    )
    client.set_async_httpx_client(
        httpx.AsyncClient(base_url="https://example.test", headers=headers, transport=httpx.MockTransport(handle))
    )
    with client:
        list_events.sync_detailed(client=client)
    async with client:
        await list_events.asyncio_detailed(client=client)
    expected = "application/vnd.x+json" if accept == "application/vnd.x+json" else "application/json"
    assert len(requests) == 2
    for request in requests:
        assert [value.decode() for key, value in request.headers.raw if key.lower() == b"accept"] == [expected]


async def test_new_workspace_404_operations_parse_api_route_not_found_in_all_call_modes() -> None:
    observed: list[tuple[str, str]] = []

    def handle(request: httpx.Request) -> httpx.Response:
        assert request.url.host == "127.0.0.1"
        path = request.url.path.removeprefix("/api/v1")
        observed.append((request.method, path))
        return httpx.Response(
            404,
            json={
                "error": {
                    "code": "api_route_not_found",
                    "message": "Workspace is nonexistent, inaccessible or noncanonical.",
                    "resolution": "Check the workspace selector and retry.",
                },
                "request": {"method": request.method, "path": path},
                "resources": {"documentation": "https://plainrouter.com/docs", "openapi": "https://plainrouter.com/openapi.json"},
            },
        )

    transport = httpx.MockTransport(handle)
    client = create_client(
        "workspace-404-test",
        base_url="http://127.0.0.1:4567/api/v1",
        httpx_args={"transport": transport},
    )

    def import_body() -> DraftBatchFileImportRequest:
        return DraftBatchFileImportRequest(
            file=File(payload=BytesIO(b"image")),
            source_adset_id="123",
            source_ad_id="456",
            mode=DraftBatchMode.DUPLICATE_ADSET,
        )

    for result in [
        agent_context_api.sync(client=client),
        agent_context_api.sync_detailed(client=client).parsed,
        launcher_file_import.sync(client=client, body=import_body()),
        launcher_file_import.sync_detailed(client=client, body=import_body()).parsed,
    ]:
        assert isinstance(result, ApiRouteNotFound)
        assert result.error.code.value == "api_route_not_found"

    async with client:
        context = await agent_context_api.asyncio(client=client)
        context_response = await agent_context_api.asyncio_detailed(client=client)
        file_import = await launcher_file_import.asyncio(client=client, body=import_body())
        file_import_response = await launcher_file_import.asyncio_detailed(client=client, body=import_body())

    for result in [context, context_response.parsed, file_import, file_import_response.parsed]:
        assert isinstance(result, ApiRouteNotFound)
        assert result.error.code.value == "api_route_not_found"
    assert context_response.status_code == 404
    assert file_import_response.status_code == 404
    assert observed == [
        ("GET", "/agent/context"),
        ("GET", "/agent/context"),
        ("POST", "/mcp/launcher/import"),
        ("POST", "/mcp/launcher/import"),
        ("GET", "/agent/context"),
        ("GET", "/agent/context"),
        ("POST", "/mcp/launcher/import"),
        ("POST", "/mcp/launcher/import"),
    ]


@pytest.mark.parametrize("base,expected", [
    (None, "/mcp/launcher/import"),
    ("https://proxy.example/api/v1", "/mcp/launcher/import"),
    ("https://proxy.example/api/v1/", "/mcp/launcher/import"),
    ("https://proxy.example/prefix/api/v1", "/prefix/mcp/launcher/import"),
    ("https://proxy.example/api/v1beta", "/api/v1beta/mcp/launcher/import"),
    ("https://proxy.example/api/v1/inner", "/api/v1/inner/mcp/launcher/import"),
    ("http://127.0.0.1:8080", "/mcp/launcher/import"),
])
async def test_launcher_import_route_on_loopback(base: str | None, expected: str) -> None:
    paths: list[str] = []

    class Capture(BaseHTTPRequestHandler):
        def do_POST(self) -> None:
            paths.append(self.path)
            self.rfile.read(int(self.headers["Content-Length"]))
            body = b'{"message":"Unauthenticated."}'
            self.send_response(401)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, format: str, *args: object) -> None:
            pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Capture)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    transport = httpx.HTTPTransport(trust_env=False)

    def redirect(request: httpx.Request) -> httpx.Response:
        request.read()
        request.url = request.url.copy_with(scheme="http", host="127.0.0.1", port=server.server_port)
        response = transport.handle_request(request)
        response.read()
        return httpx.Response(response.status_code, headers=response.headers, content=response.content)

    client = create_client("loopback") if base is None else create_client("loopback", base_url=base)
    logical_base = client._base_url
    client.set_httpx_client(httpx.Client(base_url=logical_base, transport=httpx.MockTransport(redirect)))
    client.set_async_httpx_client(httpx.AsyncClient(base_url=logical_base, transport=httpx.MockTransport(redirect)))

    def body() -> DraftBatchFileImportRequest:
        return DraftBatchFileImportRequest(file=File(payload=BytesIO(b"image")), source_adset_id="123", source_ad_id="456", mode=DraftBatchMode.DUPLICATE_ADSET)

    try:
        launcher_file_import.sync(client=client, body=body())
        launcher_file_import.sync_detailed(client=client, body=body())
        await launcher_file_import.asyncio(client=client, body=body())
        await launcher_file_import.asyncio_detailed(client=client, body=body())
        assert paths == [expected] * 4
    finally:
        client.get_httpx_client().close()
        await client.get_async_httpx_client().aclose()
        transport.close()
        server.shutdown()
        server.server_close()
        thread.join()
