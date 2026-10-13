from __future__ import annotations

import ssl
from typing import Any

import httpx
from attrs import define

from .generated import AuthenticatedClient as GeneratedAuthenticatedClient
from .generated import Client as GeneratedClient


def _reject_redirect(response: httpx.Response) -> None:
    if 300 <= response.status_code < 400:
        raise httpx.HTTPStatusError(
            f"API request returned HTTP {response.status_code}", request=response.request, response=response
        )


async def _reject_redirect_async(response: httpx.Response) -> None:
    _reject_redirect(response)


def _json_headers(headers: dict[str, str]) -> dict[str, str]:
    result = httpx.Headers({"Accept": "application/json"})
    result.update(headers)
    return dict(result)


def _sync_client(client: httpx.Client) -> httpx.Client:
    if _reject_redirect not in client.event_hooks["response"]:
        client.event_hooks["response"].insert(0, _reject_redirect)
    return client


def _async_client(client: httpx.AsyncClient) -> httpx.AsyncClient:
    if _reject_redirect_async not in client.event_hooks["response"]:
        client.event_hooks["response"].insert(0, _reject_redirect_async)
    return client


@define
class AuthenticatedClient(GeneratedAuthenticatedClient):
    """JSON API client that rejects redirects before generated response parsing."""

    def __attrs_post_init__(self) -> None:
        self._headers = _json_headers(self._headers)

    def get_httpx_client(self) -> httpx.Client:
        return _sync_client(super().get_httpx_client())

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        return _async_client(super().get_async_httpx_client())


@define
class Client(GeneratedClient):
    """Zero-auth JSON API client with the same redirect protection."""

    def __attrs_post_init__(self) -> None:
        self._headers = _json_headers(self._headers)

    def get_httpx_client(self) -> httpx.Client:
        return _sync_client(super().get_httpx_client())

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        return _async_client(super().get_async_httpx_client())


DEFAULT_BASE_URL = "https://plainrouter.com/api/v1"


def create_client(
    signal_tracker_secret: str,
    *,
    base_url: str = DEFAULT_BASE_URL,
    timeout: httpx.Timeout | None = None,
    verify_ssl: str | bool | ssl.SSLContext = True,
    follow_redirects: bool = False,
    raise_on_unexpected_status: bool = False,
    httpx_args: dict[str, Any] | None = None,
) -> AuthenticatedClient:
    """Create a client authenticated with the bearer token required by the operation."""

    return AuthenticatedClient(
        base_url=base_url,
        token=signal_tracker_secret,
        timeout=httpx.Timeout(30.0) if timeout is None else timeout,
        verify_ssl=verify_ssl,
        follow_redirects=follow_redirects,
        raise_on_unexpected_status=raise_on_unexpected_status,
        httpx_args={} if httpx_args is None else httpx_args,
    )
