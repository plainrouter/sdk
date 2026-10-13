from __future__ import annotations

import ssl
from typing import Any

import httpx
from attrs import define, evolve

from .generated import AuthenticatedClient as GeneratedAuthenticatedClient
from .generated import Client as GeneratedClient


def _reject_redirect(response: httpx.Response) -> None:
    if 300 <= response.status_code < 400:
        raise httpx.HTTPStatusError(
            f"API request returned HTTP {response.status_code}", request=response.request, response=response
        )


async def _reject_redirect_async(response: httpx.Response) -> None:
    _reject_redirect(response)


def _merge_headers(*sources: dict[str, str]) -> dict[str, str]:
    # Preserve the winning spelling, but replace by case-insensitive name.
    result: dict[str, tuple[str, str]] = {}
    for source in sources:
        for name, value in source.items():
            result[name.lower()] = (name, value)
    return dict(result.values())


def _json_headers(headers: dict[str, str]) -> dict[str, str]:
    return _merge_headers({"Accept": "application/json"}, headers)


def _injected_headers(client: httpx.Client | httpx.AsyncClient) -> None:
    if client.headers.get("Accept") in (None, "*/*"):
        client.headers["Accept"] = "application/json"


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

    def with_headers(self, headers: dict[str, str]) -> "AuthenticatedClient":
        if self._client is not None:
            self._client.headers.update(_merge_headers(headers))
        if self._async_client is not None:
            self._async_client.headers.update(_merge_headers(headers))
        return evolve(self, headers=_merge_headers(self._headers, headers))

    def set_httpx_client(self, client: httpx.Client) -> "AuthenticatedClient":
        _injected_headers(client)
        self._client = client
        return self

    def set_async_httpx_client(self, async_client: httpx.AsyncClient) -> "AuthenticatedClient":
        _injected_headers(async_client)
        self._async_client = async_client
        return self

    def get_httpx_client(self) -> httpx.Client:
        self._headers = _merge_headers(
            self._headers, {self.auth_header_name: f"{self.prefix} {self.token}" if self.prefix else self.token}
        )
        return _sync_client(super().get_httpx_client())

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        self._headers = _merge_headers(
            self._headers, {self.auth_header_name: f"{self.prefix} {self.token}" if self.prefix else self.token}
        )
        return _async_client(super().get_async_httpx_client())


@define
class Client(GeneratedClient):
    """Zero-auth JSON API client with the same redirect protection."""

    def __attrs_post_init__(self) -> None:
        self._headers = _json_headers(self._headers)

    def with_headers(self, headers: dict[str, str]) -> "Client":
        if self._client is not None:
            self._client.headers.update(_merge_headers(headers))
        if self._async_client is not None:
            self._async_client.headers.update(_merge_headers(headers))
        return evolve(self, headers=_merge_headers(self._headers, headers))

    def set_httpx_client(self, client: httpx.Client) -> "Client":
        _injected_headers(client)
        self._client = client
        return self

    def set_async_httpx_client(self, async_client: httpx.AsyncClient) -> "Client":
        _injected_headers(async_client)
        self._async_client = async_client
        return self

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
