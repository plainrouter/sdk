from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_message import ErrorMessage
from ...models.send_test_purchase_body import SendTestPurchaseBody
from ...models.send_test_purchase_response_200 import SendTestPurchaseResponse200
from ...models.send_test_purchase_response_502 import SendTestPurchaseResponse502
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    destination: str,
    *,
    body: SendTestPurchaseBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/destinations/{destination}/test-purchase".format(
            destination=quote(str(destination), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorMessage | ErrorMessage | ValidationError | SendTestPurchaseResponse200 | SendTestPurchaseResponse502 | None:
    if response.status_code == 200:
        response_200 = SendTestPurchaseResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorMessage.from_dict(response.json())

        return response_404

    if response.status_code == 422:

        def _parse_response_422(data: object) -> ErrorMessage | ValidationError:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = ErrorMessage.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_1 = ValidationError.from_dict(data)

            return response_422_type_1

        response_422 = _parse_response_422(response.json())

        return response_422

    if response.status_code == 502:
        response_502 = SendTestPurchaseResponse502.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ErrorMessage | ErrorMessage | ValidationError | SendTestPurchaseResponse200 | SendTestPurchaseResponse502
]:
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
    body: SendTestPurchaseBody | Unset = UNSET,
) -> Response[
    ErrorMessage | ErrorMessage | ValidationError | SendTestPurchaseResponse200 | SendTestPurchaseResponse502
]:
    """
    Args:
        destination (str):
        body (SendTestPurchaseBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | ErrorMessage | ValidationError | SendTestPurchaseResponse200 | SendTestPurchaseResponse502]
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
    body: SendTestPurchaseBody | Unset = UNSET,
) -> ErrorMessage | ErrorMessage | ValidationError | SendTestPurchaseResponse200 | SendTestPurchaseResponse502 | None:
    """
    Args:
        destination (str):
        body (SendTestPurchaseBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | ErrorMessage | ValidationError | SendTestPurchaseResponse200 | SendTestPurchaseResponse502
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
    body: SendTestPurchaseBody | Unset = UNSET,
) -> Response[
    ErrorMessage | ErrorMessage | ValidationError | SendTestPurchaseResponse200 | SendTestPurchaseResponse502
]:
    """
    Args:
        destination (str):
        body (SendTestPurchaseBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | ErrorMessage | ValidationError | SendTestPurchaseResponse200 | SendTestPurchaseResponse502]
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
    body: SendTestPurchaseBody | Unset = UNSET,
) -> ErrorMessage | ErrorMessage | ValidationError | SendTestPurchaseResponse200 | SendTestPurchaseResponse502 | None:
    """
    Args:
        destination (str):
        body (SendTestPurchaseBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | ErrorMessage | ValidationError | SendTestPurchaseResponse200 | SendTestPurchaseResponse502
    """

    return (
        await asyncio_detailed(
            destination=destination,
            client=client,
            body=body,
        )
    ).parsed
