from __future__ import annotations

from collections.abc import Mapping
from typing import cast

from .generated.api.event import create_event as _generated_create_event
from .generated.client import AuthenticatedClient, Client
from .generated.models.create_event_body_type_0 import CreateEventBodyType0
from .generated.models.create_event_body_type_1 import CreateEventBodyType1
from .generated.models.create_event_response_200 import CreateEventResponse200
from .generated.models.create_event_response_202 import CreateEventResponse202
from .generated.models.error_message import ErrorMessage
from .generated.models.validation_error import ValidationError
from .generated.types import UNSET, Response, Unset
from .validation import validate_create_event_body

CreateEventBody = CreateEventBodyType0 | CreateEventBodyType1
CreateEventBodyInput = CreateEventBody | Mapping[str, object]
CreateEventResponse = CreateEventResponse200 | CreateEventResponse202 | ErrorMessage | ValidationError


class _RawCreateEventBody:
    """Adapt a raw JSON mapping to the generated client's body protocol."""

    def __init__(self, body: Mapping[str, object]) -> None:
        self._body = dict(body)

    def to_dict(self) -> dict[str, object]:
        """Return the caller's payload without changing nested values."""

        return dict(self._body)


def _prepare_body(body: CreateEventBodyInput) -> CreateEventBody:
    validate_create_event_body(body)

    if isinstance(body, Mapping):
        return cast(CreateEventBody, _RawCreateEventBody(body))

    return body


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateEventBodyInput,
    idempotency_key: str | Unset = UNSET,
) -> Response[CreateEventResponse]:
    """Submit a conversion event after validating its identity capture time."""

    prepared_body = _prepare_body(body)

    return _generated_create_event.sync_detailed(
        client=client,
        body=prepared_body,
        idempotency_key=idempotency_key,
    )


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateEventBodyInput,
    idempotency_key: str | Unset = UNSET,
) -> CreateEventResponse | None:
    """Submit a conversion event after validating its identity capture time."""

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateEventBodyInput,
    idempotency_key: str | Unset = UNSET,
) -> Response[CreateEventResponse]:
    """Submit a conversion event asynchronously after validating its identity capture time."""

    prepared_body = _prepare_body(body)

    return await _generated_create_event.asyncio_detailed(
        client=client,
        body=prepared_body,
        idempotency_key=idempotency_key,
    )


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateEventBodyInput,
    idempotency_key: str | Unset = UNSET,
) -> CreateEventResponse | None:
    """Submit a conversion event asynchronously after validating its identity capture time."""

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed


__all__ = (
    "CreateEventBody",
    "CreateEventBodyInput",
    "CreateEventResponse",
    "asyncio",
    "asyncio_detailed",
    "sync",
    "sync_detailed",
)
