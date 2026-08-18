from collections.abc import Generator
from typing import Any

import pytest


@pytest.fixture(autouse=True)
def prohibit_network(monkeypatch: pytest.MonkeyPatch) -> Generator[None, None, None]:
    """Make accidental socket access fail even if a test forgets its mock transport."""

    def fail_network(*args: Any, **kwargs: Any) -> None:
        raise AssertionError("Network access is prohibited in the Python SDK test suite")

    monkeypatch.setattr("socket.socket.connect", fail_network)
    yield
