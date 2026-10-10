import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_message import ErrorMessage
from ...models.get_inventory_metrics_response_200 import GetInventoryMetricsResponse200
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: int,
    account_id: str,
    *,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    campaign_id: None | str | Unset = UNSET,
    adset_id: None | str | Unset = UNSET,
    ad_id: None | str | Unset = UNSET,
    include_changes: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_start_date: None | str | Unset
    if isinstance(start_date, Unset):
        json_start_date = UNSET
    elif isinstance(start_date, datetime.date):
        json_start_date = start_date.isoformat()
    else:
        json_start_date = start_date
    params["start_date"] = json_start_date

    json_end_date: None | str | Unset
    if isinstance(end_date, Unset):
        json_end_date = UNSET
    elif isinstance(end_date, datetime.date):
        json_end_date = end_date.isoformat()
    else:
        json_end_date = end_date
    params["end_date"] = json_end_date

    json_campaign_id: None | str | Unset
    if isinstance(campaign_id, Unset):
        json_campaign_id = UNSET
    else:
        json_campaign_id = campaign_id
    params["campaign_id"] = json_campaign_id

    json_adset_id: None | str | Unset
    if isinstance(adset_id, Unset):
        json_adset_id = UNSET
    else:
        json_adset_id = adset_id
    params["adset_id"] = json_adset_id

    json_ad_id: None | str | Unset
    if isinstance(ad_id, Unset):
        json_ad_id = UNSET
    else:
        json_ad_id = ad_id
    params["ad_id"] = json_ad_id

    params["include_changes"] = include_changes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace}/admin/ad-accounts/{account_id}/inventory/metrics".format(
            workspace=quote(str(workspace), safe=""),
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorMessage | GetInventoryMetricsResponse200 | ValidationError | None:
    if response.status_code == 200:
        response_200 = GetInventoryMetricsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorMessage.from_dict(response.json())

        return response_403

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
) -> Response[ErrorMessage | GetInventoryMetricsResponse200 | ValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: int,
    account_id: str,
    *,
    client: AuthenticatedClient,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    campaign_id: None | str | Unset = UNSET,
    adset_id: None | str | Unset = UNSET,
    ad_id: None | str | Unset = UNSET,
    include_changes: bool | Unset = UNSET,
) -> Response[ErrorMessage | GetInventoryMetricsResponse200 | ValidationError]:
    """Compare Meta metrics with counted arrivals

     Compare daily Meta metrics with PlainRouter arrivals in the account timezone, within plan retention.
    Unknown object IDs are never exposed.

    Args:
        workspace (int):
        account_id (str):
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        campaign_id (None | str | Unset):
        adset_id (None | str | Unset):
        ad_id (None | str | Unset):
        include_changes (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | GetInventoryMetricsResponse200 | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        account_id=account_id,
        start_date=start_date,
        end_date=end_date,
        campaign_id=campaign_id,
        adset_id=adset_id,
        ad_id=ad_id,
        include_changes=include_changes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: int,
    account_id: str,
    *,
    client: AuthenticatedClient,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    campaign_id: None | str | Unset = UNSET,
    adset_id: None | str | Unset = UNSET,
    ad_id: None | str | Unset = UNSET,
    include_changes: bool | Unset = UNSET,
) -> ErrorMessage | GetInventoryMetricsResponse200 | ValidationError | None:
    """Compare Meta metrics with counted arrivals

     Compare daily Meta metrics with PlainRouter arrivals in the account timezone, within plan retention.
    Unknown object IDs are never exposed.

    Args:
        workspace (int):
        account_id (str):
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        campaign_id (None | str | Unset):
        adset_id (None | str | Unset):
        ad_id (None | str | Unset):
        include_changes (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | GetInventoryMetricsResponse200 | ValidationError
    """

    return sync_detailed(
        workspace=workspace,
        account_id=account_id,
        client=client,
        start_date=start_date,
        end_date=end_date,
        campaign_id=campaign_id,
        adset_id=adset_id,
        ad_id=ad_id,
        include_changes=include_changes,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    account_id: str,
    *,
    client: AuthenticatedClient,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    campaign_id: None | str | Unset = UNSET,
    adset_id: None | str | Unset = UNSET,
    ad_id: None | str | Unset = UNSET,
    include_changes: bool | Unset = UNSET,
) -> Response[ErrorMessage | GetInventoryMetricsResponse200 | ValidationError]:
    """Compare Meta metrics with counted arrivals

     Compare daily Meta metrics with PlainRouter arrivals in the account timezone, within plan retention.
    Unknown object IDs are never exposed.

    Args:
        workspace (int):
        account_id (str):
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        campaign_id (None | str | Unset):
        adset_id (None | str | Unset):
        ad_id (None | str | Unset):
        include_changes (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | GetInventoryMetricsResponse200 | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        account_id=account_id,
        start_date=start_date,
        end_date=end_date,
        campaign_id=campaign_id,
        adset_id=adset_id,
        ad_id=ad_id,
        include_changes=include_changes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    account_id: str,
    *,
    client: AuthenticatedClient,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    campaign_id: None | str | Unset = UNSET,
    adset_id: None | str | Unset = UNSET,
    ad_id: None | str | Unset = UNSET,
    include_changes: bool | Unset = UNSET,
) -> ErrorMessage | GetInventoryMetricsResponse200 | ValidationError | None:
    """Compare Meta metrics with counted arrivals

     Compare daily Meta metrics with PlainRouter arrivals in the account timezone, within plan retention.
    Unknown object IDs are never exposed.

    Args:
        workspace (int):
        account_id (str):
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        campaign_id (None | str | Unset):
        adset_id (None | str | Unset):
        ad_id (None | str | Unset):
        include_changes (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | GetInventoryMetricsResponse200 | ValidationError
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            account_id=account_id,
            client=client,
            start_date=start_date,
            end_date=end_date,
            campaign_id=campaign_id,
            adset_id=adset_id,
            ad_id=ad_id,
            include_changes=include_changes,
        )
    ).parsed
