from __future__ import annotations

import ssl
from typing import Any

import httpx

from .generated import AuthenticatedClient

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
    """Create a client authenticated with a Signal Tracker secret."""

    return AuthenticatedClient(
        base_url=base_url,
        token=signal_tracker_secret,
        timeout=timeout,
        verify_ssl=verify_ssl,
        follow_redirects=follow_redirects,
        raise_on_unexpected_status=raise_on_unexpected_status,
        httpx_args={} if httpx_args is None else httpx_args,
    )
