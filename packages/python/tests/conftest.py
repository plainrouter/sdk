import ipaddress
import socket
from collections.abc import Generator
from typing import Any

import pytest


@pytest.fixture(autouse=True)
def prohibit_network(monkeypatch: pytest.MonkeyPatch) -> Generator[None, None, None]:
    """Permit capture servers on loopback and refuse every external connection."""

    connect = socket.socket.connect

    def fail_network(sock: socket.socket, address: Any) -> None:
        if isinstance(address, tuple) and ipaddress.ip_address(address[0]).is_loopback:
            connect(sock, address)
            return
        raise AssertionError("Non-loopback network access is prohibited in the Python SDK test suite")

    monkeypatch.setattr("socket.socket.connect", fail_network)
    yield
