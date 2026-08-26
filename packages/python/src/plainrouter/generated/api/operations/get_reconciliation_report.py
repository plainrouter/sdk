import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_message import ErrorMessage
from ...models.get_reconciliation_report_response_200 import GetReconciliationReportResponse200
from ...models.validation_error import ValidationError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    date: datetime.date,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_date = date.isoformat()
    params["date"] = json_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/reports/reconciliation",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorMessage | GetReconciliationReportResponse200 | ValidationError | None:
    if response.status_code == 200:
        response_200 = GetReconciliationReportResponse200.from_dict(response.json())

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
) -> Response[ErrorMessage | GetReconciliationReportResponse200 | ValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    date: datetime.date,
) -> Response[ErrorMessage | GetReconciliationReportResponse200 | ValidationError]:
    """Get a reconciliation report

     Returns stored delivery-versus-platform reconciliation results for one calendar date.

    Args:
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | GetReconciliationReportResponse200 | ValidationError]
    """

    kwargs = _get_kwargs(
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    date: datetime.date,
) -> ErrorMessage | GetReconciliationReportResponse200 | ValidationError | None:
    """Get a reconciliation report

     Returns stored delivery-versus-platform reconciliation results for one calendar date.

    Args:
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | GetReconciliationReportResponse200 | ValidationError
    """

    return sync_detailed(
        client=client,
        date=date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    date: datetime.date,
) -> Response[ErrorMessage | GetReconciliationReportResponse200 | ValidationError]:
    """Get a reconciliation report

     Returns stored delivery-versus-platform reconciliation results for one calendar date.

    Args:
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | GetReconciliationReportResponse200 | ValidationError]
    """

    kwargs = _get_kwargs(
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    date: datetime.date,
) -> ErrorMessage | GetReconciliationReportResponse200 | ValidationError | None:
    """Get a reconciliation report

     Returns stored delivery-versus-platform reconciliation results for one calendar date.

    Args:
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | GetReconciliationReportResponse200 | ValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
        )
    ).parsed
