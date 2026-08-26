from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.validate_sandbox_event_body import ValidateSandboxEventBody
from ...models.validate_sandbox_event_response_200 import ValidateSandboxEventResponse200
from ...models.validation_error import ValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: ValidateSandboxEventBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/sandbox/events",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ValidateSandboxEventResponse200 | ValidationError | None:
    if response.status_code == 200:
        response_200 = ValidateSandboxEventResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = ValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ValidateSandboxEventResponse200 | ValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ValidateSandboxEventBody,
) -> Response[ValidateSandboxEventResponse200 | ValidationError]:
    """Validate a synthetic event

     Validates and immediately discards one identity-free synthetic event. It requires no account or API
    key and never writes to the ledger or contacts Meta.

    Args:
        body (ValidateSandboxEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ValidateSandboxEventResponse200 | ValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ValidateSandboxEventBody,
) -> ValidateSandboxEventResponse200 | ValidationError | None:
    """Validate a synthetic event

     Validates and immediately discards one identity-free synthetic event. It requires no account or API
    key and never writes to the ledger or contacts Meta.

    Args:
        body (ValidateSandboxEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ValidateSandboxEventResponse200 | ValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ValidateSandboxEventBody,
) -> Response[ValidateSandboxEventResponse200 | ValidationError]:
    """Validate a synthetic event

     Validates and immediately discards one identity-free synthetic event. It requires no account or API
    key and never writes to the ledger or contacts Meta.

    Args:
        body (ValidateSandboxEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ValidateSandboxEventResponse200 | ValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ValidateSandboxEventBody,
) -> ValidateSandboxEventResponse200 | ValidationError | None:
    """Validate a synthetic event

     Validates and immediately discards one identity-free synthetic event. It requires no account or API
    key and never writes to the ledger or contacts Meta.

    Args:
        body (ValidateSandboxEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ValidateSandboxEventResponse200 | ValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
