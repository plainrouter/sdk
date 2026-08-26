from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_user_data_body import DeleteUserDataBody
from ...models.delete_user_data_response_200 import DeleteUserDataResponse200
from ...models.error_message import ErrorMessage
from ...models.validation_error import ValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: DeleteUserDataBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/user-data",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteUserDataResponse200 | ErrorMessage | ValidationError | None:
    if response.status_code == 200:
        response_200 = DeleteUserDataResponse200.from_dict(response.json())

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
) -> Response[DeleteUserDataResponse200 | ErrorMessage | ValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteUserDataBody,
) -> Response[DeleteUserDataResponse200 | ErrorMessage | ValidationError]:
    """Delete user data by hashed identifier

     Idempotently removes retained user data matching one caller-supplied SHA-256 identifier digest.

    Args:
        body (DeleteUserDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteUserDataResponse200 | ErrorMessage | ValidationError]
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
    body: DeleteUserDataBody,
) -> DeleteUserDataResponse200 | ErrorMessage | ValidationError | None:
    """Delete user data by hashed identifier

     Idempotently removes retained user data matching one caller-supplied SHA-256 identifier digest.

    Args:
        body (DeleteUserDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteUserDataResponse200 | ErrorMessage | ValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteUserDataBody,
) -> Response[DeleteUserDataResponse200 | ErrorMessage | ValidationError]:
    """Delete user data by hashed identifier

     Idempotently removes retained user data matching one caller-supplied SHA-256 identifier digest.

    Args:
        body (DeleteUserDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteUserDataResponse200 | ErrorMessage | ValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteUserDataBody,
) -> DeleteUserDataResponse200 | ErrorMessage | ValidationError | None:
    """Delete user data by hashed identifier

     Idempotently removes retained user data matching one caller-supplied SHA-256 identifier digest.

    Args:
        body (DeleteUserDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteUserDataResponse200 | ErrorMessage | ValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
