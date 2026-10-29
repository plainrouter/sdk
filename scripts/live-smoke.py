from __future__ import annotations

import os
from http import HTTPStatus

from plainrouter import DEFAULT_BASE_URL, Client, list_events
from plainrouter.generated.models.error_message import ErrorMessage


def main() -> None:
    base_url = os.environ.get("PLAINROUTER_BASE_URL") or DEFAULT_BASE_URL
    with Client(base_url=base_url, raise_on_unexpected_status=True) as anonymous:
        response = list_events.sync_detailed(client=anonymous, per_page=1)

    if response.status_code != HTTPStatus.UNAUTHORIZED:
        raise RuntimeError(f"Anonymous event listing must return HTTP 401, received {response.status_code}.")
    if not isinstance(response.parsed, ErrorMessage) or not isinstance(response.parsed.message, str):
        raise RuntimeError("Anonymous event listing returned an invalid authentication error.")
    if not response.parsed.message.strip():
        raise RuntimeError("Anonymous event listing returned an empty authentication error.")

    print("Python SDK anonymous authorization smoke passed (401). No authenticated operations exercised.")


if __name__ == "__main__":
    main()
