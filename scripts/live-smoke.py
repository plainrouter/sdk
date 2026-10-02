from __future__ import annotations

import os

from plainrouter import DEFAULT_BASE_URL, create_client, list_events
from plainrouter.generated import AuthenticatedClient, Client
from plainrouter.generated.api.sandbox import (
    get_sandbox,
    validate_sandbox_event,
    validate_sandbox_event_with_key,
)
from plainrouter.generated.models import (
    GetSandboxResponse200,
    ListEventsResponse200,
    ValidateSandboxEventBody,
    ValidateSandboxEventResponse200,
    ValidateSandboxEventWithKeyBody,
    ValidateSandboxEventWithKeyResponse200,
)


def assert_discarded(
    result: object,
    expected: type[ValidateSandboxEventResponse200] | type[ValidateSandboxEventWithKeyResponse200],
    description: str,
) -> None:
    if not isinstance(result, expected):
        raise RuntimeError(f"{description} returned an unexpected response: {result!r}")
    if not (result.sandbox and result.accepted) or result.persisted or result.provider_delivery:
        raise RuntimeError(f"{description} was not validated and discarded: {result.to_dict()}")


def main() -> None:
    base_url = os.environ.get("PLAINROUTER_BASE_URL") or DEFAULT_BASE_URL

    anonymous = Client(base_url=base_url, raise_on_unexpected_status=True)
    sandbox = get_sandbox.sync(client=anonymous)
    if not isinstance(sandbox, GetSandboxResponse200):
        raise RuntimeError(f"Sandbox discovery returned an unexpected response: {sandbox!r}")
    if sandbox.persists_data or sandbox.provider_delivery:
        raise RuntimeError("The live sandbox no longer declares itself isolated.")

    body = sandbox.try_.body.to_dict()
    assert_discarded(
        validate_sandbox_event.sync(client=anonymous, body=ValidateSandboxEventBody.from_dict(body)),
        ValidateSandboxEventResponse200,
        "Zero-auth synthetic event",
    )

    keyed = AuthenticatedClient(
        base_url=base_url,
        token=sandbox.self_serve_key.issued_key.api_key,
        raise_on_unexpected_status=True,
    )
    assert_discarded(
        validate_sandbox_event_with_key.sync(client=keyed, body=ValidateSandboxEventWithKeyBody.from_dict(body)),
        ValidateSandboxEventWithKeyResponse200,
        "Keyed synthetic event",
    )
    print("Python SDK live sandbox smoke passed.")

    signal_tracker_secret = os.environ.get("PLAINROUTER_SMOKE_SECRET")
    if not signal_tracker_secret:
        print(
            "::notice title=Authenticated live smoke skipped::PLAINROUTER_SMOKE_SECRET is not set; "
            "only the zero-auth sandbox was exercised."
        )
        return

    events = list_events.sync(
        client=create_client(signal_tracker_secret, base_url=base_url, raise_on_unexpected_status=True),
        per_page=5,
    )
    if not isinstance(events, ListEventsResponse200):
        raise RuntimeError(f"Authenticated event listing returned an unexpected response: {events!r}")
    print("Python SDK live authenticated read smoke passed.")


if __name__ == "__main__":
    main()
