from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_message import ErrorMessage
from ...models.validate_sandbox_event_with_key_body import ValidateSandboxEventWithKeyBody
from ...models.validate_sandbox_event_with_key_response_200 import ValidateSandboxEventWithKeyResponse200
from ...models.validation_error import ValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: ValidateSandboxEventWithKeyBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/sandbox/keyed-events",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorMessage | ValidateSandboxEventWithKeyResponse200 | ValidationError | None:
    if response.status_code == 200:
        response_200 = ValidateSandboxEventWithKeyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

    if response.status_code == 422:
        response_422 = ValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorMessage | ValidateSandboxEventWithKeyResponse200 | ValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ValidateSandboxEventWithKeyBody,
) -> Response[ErrorMessage | ValidateSandboxEventWithKeyResponse200 | ValidationError]:
    """Validate a synthetic event with a sandbox key

     Validates a synthetic event using the short-lived key returned by the self-serve sandbox key
    endpoint. It never persists data or contacts an advertising provider.

    Args:
        body (ValidateSandboxEventWithKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | ValidateSandboxEventWithKeyResponse200 | ValidationError]
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
    client: AuthenticatedClient,
    body: ValidateSandboxEventWithKeyBody,
) -> ErrorMessage | ValidateSandboxEventWithKeyResponse200 | ValidationError | None:
    """Validate a synthetic event with a sandbox key

     Validates a synthetic event using the short-lived key returned by the self-serve sandbox key
    endpoint. It never persists data or contacts an advertising provider.

    Args:
        body (ValidateSandboxEventWithKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | ValidateSandboxEventWithKeyResponse200 | ValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ValidateSandboxEventWithKeyBody,
) -> Response[ErrorMessage | ValidateSandboxEventWithKeyResponse200 | ValidationError]:
    """Validate a synthetic event with a sandbox key

     Validates a synthetic event using the short-lived key returned by the self-serve sandbox key
    endpoint. It never persists data or contacts an advertising provider.

    Args:
        body (ValidateSandboxEventWithKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | ValidateSandboxEventWithKeyResponse200 | ValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ValidateSandboxEventWithKeyBody,
) -> ErrorMessage | ValidateSandboxEventWithKeyResponse200 | ValidationError | None:
    """Validate a synthetic event with a sandbox key

     Validates a synthetic event using the short-lived key returned by the self-serve sandbox key
    endpoint. It never persists data or contacts an advertising provider.

    Args:
        body (ValidateSandboxEventWithKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | ValidateSandboxEventWithKeyResponse200 | ValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
