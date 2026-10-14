from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.actions_rules_index_response_200 import ActionsRulesIndexResponse200
from ...models.actions_rules_index_response_403_type_1 import ActionsRulesIndexResponse403Type1
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.error_message import ErrorMessage
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: int,
    *,
    page: int | Unset = UNSET,
    account_id: int | Unset = UNSET,
    platform_ad_account_id: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["account_id"] = account_id

    params["platform_ad_account_id"] = platform_ad_account_id

    params["cursor"] = cursor

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agent/workspaces/{workspace}/action-rules".format(
            workspace=quote(str(workspace), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ActionsRulesIndexResponse200
    | ActionsRulesIndexResponse403Type1
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ValidationError
    | None
):
    if response.status_code == 200:
        response_200 = ActionsRulesIndexResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

    if response.status_code == 403:

        def _parse_response_403(data: object) -> ActionsRulesIndexResponse403Type1 | ErrorMessage:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_0 = ErrorMessage.from_dict(data)

                return response_403_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_403_type_1 = ActionsRulesIndexResponse403Type1.from_dict(data)

            return response_403_type_1

        response_403 = _parse_response_403(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiRouteNotFound.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ErrorMessage.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ActionsRulesIndexResponse200
    | ActionsRulesIndexResponse403Type1
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    account_id: int | Unset = UNSET,
    platform_ad_account_id: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Response[
    ActionsRulesIndexResponse200
    | ActionsRulesIndexResponse403Type1
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ValidationError
]:
    """List rule summaries

     Read rule summaries, current revision and last-run status without histories or decisions. Continue
    with cursor; use actions.rules.show for detail.

    Args:
        workspace (int):
        page (int | Unset):
        account_id (int | Unset):
        platform_ad_account_id (int | Unset):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionsRulesIndexResponse200 | ActionsRulesIndexResponse403Type1 | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        page=page,
        account_id=account_id,
        platform_ad_account_id=platform_ad_account_id,
        cursor=cursor,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    account_id: int | Unset = UNSET,
    platform_ad_account_id: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> (
    ActionsRulesIndexResponse200
    | ActionsRulesIndexResponse403Type1
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ValidationError
    | None
):
    """List rule summaries

     Read rule summaries, current revision and last-run status without histories or decisions. Continue
    with cursor; use actions.rules.show for detail.

    Args:
        workspace (int):
        page (int | Unset):
        account_id (int | Unset):
        platform_ad_account_id (int | Unset):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionsRulesIndexResponse200 | ActionsRulesIndexResponse403Type1 | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        page=page,
        account_id=account_id,
        platform_ad_account_id=platform_ad_account_id,
        cursor=cursor,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    account_id: int | Unset = UNSET,
    platform_ad_account_id: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Response[
    ActionsRulesIndexResponse200
    | ActionsRulesIndexResponse403Type1
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ValidationError
]:
    """List rule summaries

     Read rule summaries, current revision and last-run status without histories or decisions. Continue
    with cursor; use actions.rules.show for detail.

    Args:
        workspace (int):
        page (int | Unset):
        account_id (int | Unset):
        platform_ad_account_id (int | Unset):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionsRulesIndexResponse200 | ActionsRulesIndexResponse403Type1 | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        page=page,
        account_id=account_id,
        platform_ad_account_id=platform_ad_account_id,
        cursor=cursor,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    account_id: int | Unset = UNSET,
    platform_ad_account_id: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> (
    ActionsRulesIndexResponse200
    | ActionsRulesIndexResponse403Type1
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ValidationError
    | None
):
    """List rule summaries

     Read rule summaries, current revision and last-run status without histories or decisions. Continue
    with cursor; use actions.rules.show for detail.

    Args:
        workspace (int):
        page (int | Unset):
        account_id (int | Unset):
        platform_ad_account_id (int | Unset):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionsRulesIndexResponse200 | ActionsRulesIndexResponse403Type1 | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            page=page,
            account_id=account_id,
            platform_ad_account_id=platform_ad_account_id,
            cursor=cursor,
            per_page=per_page,
        )
    ).parsed
