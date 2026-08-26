from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_message import ErrorMessage
from ...models.set_destination_test_mode_body import SetDestinationTestModeBody
from ...models.set_destination_test_mode_response_200 import SetDestinationTestModeResponse200
from ...models.validation_error import ValidationError
from ...types import Response


def _get_kwargs(
    destination: str,
    *,
    body: SetDestinationTestModeBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/destinations/{destination}/test-mode".format(
            destination=quote(str(destination), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorMessage | SetDestinationTestModeResponse200 | ValidationError | None:
    if response.status_code == 200:
        response_200 = SetDestinationTestModeResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorMessage.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorMessage | SetDestinationTestModeResponse200 | ValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    destination: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetDestinationTestModeBody,
) -> Response[ErrorMessage | SetDestinationTestModeResponse200 | ValidationError]:
    """Configure destination test mode

     Enables or disables Meta Test Events mode for a destination owned by the authenticated Signal
    tracker.

    Args:
        destination (str):
        body (SetDestinationTestModeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | SetDestinationTestModeResponse200 | ValidationError]
    """

    kwargs = _get_kwargs(
        destination=destination,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    destination: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetDestinationTestModeBody,
) -> ErrorMessage | SetDestinationTestModeResponse200 | ValidationError | None:
    """Configure destination test mode

     Enables or disables Meta Test Events mode for a destination owned by the authenticated Signal
    tracker.

    Args:
        destination (str):
        body (SetDestinationTestModeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | SetDestinationTestModeResponse200 | ValidationError
    """

    return sync_detailed(
        destination=destination,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    destination: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetDestinationTestModeBody,
) -> Response[ErrorMessage | SetDestinationTestModeResponse200 | ValidationError]:
    """Configure destination test mode

     Enables or disables Meta Test Events mode for a destination owned by the authenticated Signal
    tracker.

    Args:
        destination (str):
        body (SetDestinationTestModeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | SetDestinationTestModeResponse200 | ValidationError]
    """

    kwargs = _get_kwargs(
        destination=destination,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    destination: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetDestinationTestModeBody,
) -> ErrorMessage | SetDestinationTestModeResponse200 | ValidationError | None:
    """Configure destination test mode

     Enables or disables Meta Test Events mode for a destination owned by the authenticated Signal
    tracker.

    Args:
        destination (str):
        body (SetDestinationTestModeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | SetDestinationTestModeResponse200 | ValidationError
    """

    return (
        await asyncio_detailed(
            destination=destination,
            client=client,
            body=body,
        )
    ).parsed
