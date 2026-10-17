from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.error_message import ErrorMessage
from ...models.get_account_inventory_level_type_1 import GetAccountInventoryLevelType1
from ...models.get_account_inventory_level_type_2_type_1 import GetAccountInventoryLevelType2Type1
from ...models.get_account_inventory_level_type_3_type_1 import GetAccountInventoryLevelType3Type1
from ...models.get_account_inventory_response_200 import GetAccountInventoryResponse200
from ...models.get_account_inventory_response_404_type_1 import GetAccountInventoryResponse404Type1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: int,
    account_id: str,
    *,
    level: GetAccountInventoryLevelType1
    | GetAccountInventoryLevelType2Type1
    | GetAccountInventoryLevelType3Type1
    | None
    | Unset = UNSET,
    effective_status: None | str | Unset = UNSET,
    campaign_id: None | str | Unset = UNSET,
    adset_id: None | str | Unset = UNSET,
    after_id: int | Unset = UNSET,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_level: None | str | Unset
    if isinstance(level, Unset):
        json_level = UNSET
    elif isinstance(level, GetAccountInventoryLevelType1):
        json_level = level.value
    elif isinstance(level, GetAccountInventoryLevelType2Type1):
        json_level = level.value
    elif isinstance(level, GetAccountInventoryLevelType3Type1):
        json_level = level.value
    else:
        json_level = level
    params["level"] = json_level

    json_effective_status: None | str | Unset
    if isinstance(effective_status, Unset):
        json_effective_status = UNSET
    else:
        json_effective_status = effective_status
    params["effective_status"] = json_effective_status

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

    params["after_id"] = after_id

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace}/admin/ad-accounts/{account_id}/inventory".format(
            workspace=quote(str(workspace), safe=""),
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiRouteNotFound | GetAccountInventoryResponse404Type1 | ErrorMessage | GetAccountInventoryResponse200 | None:
    if response.status_code == 200:
        response_200 = GetAccountInventoryResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

    if response.status_code == 404:

        def _parse_response_404(data: object) -> ApiRouteNotFound | GetAccountInventoryResponse404Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_0 = ApiRouteNotFound.from_dict(data)

                return response_404_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_404_type_1 = GetAccountInventoryResponse404Type1.from_dict(data)

            return response_404_type_1

        response_404 = _parse_response_404(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiRouteNotFound | GetAccountInventoryResponse404Type1 | ErrorMessage | GetAccountInventoryResponse200]:
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
    client: AuthenticatedClient | Client,
    level: GetAccountInventoryLevelType1
    | GetAccountInventoryLevelType2Type1
    | GetAccountInventoryLevelType3Type1
    | None
    | Unset = UNSET,
    effective_status: None | str | Unset = UNSET,
    campaign_id: None | str | Unset = UNSET,
    adset_id: None | str | Unset = UNSET,
    after_id: int | Unset = UNSET,
    limit: int | Unset = 25,
) -> Response[ApiRouteNotFound | GetAccountInventoryResponse404Type1 | ErrorMessage | GetAccountInventoryResponse200]:
    """Read account inventory

     Read complete Meta objects with account-wide totals on every page. Continue with next_cursor as
    after_id; scope and filters stay unchanged.

    Args:
        workspace (int):
        account_id (str):
        level (GetAccountInventoryLevelType1 | GetAccountInventoryLevelType2Type1 |
            GetAccountInventoryLevelType3Type1 | None | Unset):
        effective_status (None | str | Unset):
        campaign_id (None | str | Unset):
        adset_id (None | str | Unset):
        after_id (int | Unset):
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | GetAccountInventoryResponse404Type1 | ErrorMessage | GetAccountInventoryResponse200]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        account_id=account_id,
        level=level,
        effective_status=effective_status,
        campaign_id=campaign_id,
        adset_id=adset_id,
        after_id=after_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: int,
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
    level: GetAccountInventoryLevelType1
    | GetAccountInventoryLevelType2Type1
    | GetAccountInventoryLevelType3Type1
    | None
    | Unset = UNSET,
    effective_status: None | str | Unset = UNSET,
    campaign_id: None | str | Unset = UNSET,
    adset_id: None | str | Unset = UNSET,
    after_id: int | Unset = UNSET,
    limit: int | Unset = 25,
) -> ApiRouteNotFound | GetAccountInventoryResponse404Type1 | ErrorMessage | GetAccountInventoryResponse200 | None:
    """Read account inventory

     Read complete Meta objects with account-wide totals on every page. Continue with next_cursor as
    after_id; scope and filters stay unchanged.

    Args:
        workspace (int):
        account_id (str):
        level (GetAccountInventoryLevelType1 | GetAccountInventoryLevelType2Type1 |
            GetAccountInventoryLevelType3Type1 | None | Unset):
        effective_status (None | str | Unset):
        campaign_id (None | str | Unset):
        adset_id (None | str | Unset):
        after_id (int | Unset):
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | GetAccountInventoryResponse404Type1 | ErrorMessage | GetAccountInventoryResponse200
    """

    return sync_detailed(
        workspace=workspace,
        account_id=account_id,
        client=client,
        level=level,
        effective_status=effective_status,
        campaign_id=campaign_id,
        adset_id=adset_id,
        after_id=after_id,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
    level: GetAccountInventoryLevelType1
    | GetAccountInventoryLevelType2Type1
    | GetAccountInventoryLevelType3Type1
    | None
    | Unset = UNSET,
    effective_status: None | str | Unset = UNSET,
    campaign_id: None | str | Unset = UNSET,
    adset_id: None | str | Unset = UNSET,
    after_id: int | Unset = UNSET,
    limit: int | Unset = 25,
) -> Response[ApiRouteNotFound | GetAccountInventoryResponse404Type1 | ErrorMessage | GetAccountInventoryResponse200]:
    """Read account inventory

     Read complete Meta objects with account-wide totals on every page. Continue with next_cursor as
    after_id; scope and filters stay unchanged.

    Args:
        workspace (int):
        account_id (str):
        level (GetAccountInventoryLevelType1 | GetAccountInventoryLevelType2Type1 |
            GetAccountInventoryLevelType3Type1 | None | Unset):
        effective_status (None | str | Unset):
        campaign_id (None | str | Unset):
        adset_id (None | str | Unset):
        after_id (int | Unset):
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | GetAccountInventoryResponse404Type1 | ErrorMessage | GetAccountInventoryResponse200]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        account_id=account_id,
        level=level,
        effective_status=effective_status,
        campaign_id=campaign_id,
        adset_id=adset_id,
        after_id=after_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
    level: GetAccountInventoryLevelType1
    | GetAccountInventoryLevelType2Type1
    | GetAccountInventoryLevelType3Type1
    | None
    | Unset = UNSET,
    effective_status: None | str | Unset = UNSET,
    campaign_id: None | str | Unset = UNSET,
    adset_id: None | str | Unset = UNSET,
    after_id: int | Unset = UNSET,
    limit: int | Unset = 25,
) -> ApiRouteNotFound | GetAccountInventoryResponse404Type1 | ErrorMessage | GetAccountInventoryResponse200 | None:
    """Read account inventory

     Read complete Meta objects with account-wide totals on every page. Continue with next_cursor as
    after_id; scope and filters stay unchanged.

    Args:
        workspace (int):
        account_id (str):
        level (GetAccountInventoryLevelType1 | GetAccountInventoryLevelType2Type1 |
            GetAccountInventoryLevelType3Type1 | None | Unset):
        effective_status (None | str | Unset):
        campaign_id (None | str | Unset):
        adset_id (None | str | Unset):
        after_id (int | Unset):
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | GetAccountInventoryResponse404Type1 | ErrorMessage | GetAccountInventoryResponse200
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            account_id=account_id,
            client=client,
            level=level,
            effective_status=effective_status,
            campaign_id=campaign_id,
            adset_id=adset_id,
            after_id=after_id,
            limit=limit,
        )
    ).parsed
