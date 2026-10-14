from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_rule_detail_read import ActionRuleDetailRead
from ...models.actions_rules_show_response_403_type_1 import ActionsRulesShowResponse403Type1
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.error_message import ErrorMessage
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: int,
    action_rule: str,
    *,
    account_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["account_id"] = account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agent/workspaces/{workspace}/action-rules/{action_rule}".format(
            workspace=quote(str(workspace), safe=""),
            action_rule=quote(str(action_rule), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ActionRuleDetailRead
    | ActionsRulesShowResponse403Type1
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ValidationError
    | None
):
    if response.status_code == 200:
        response_200 = ActionRuleDetailRead.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

    if response.status_code == 403:

        def _parse_response_403(data: object) -> ActionsRulesShowResponse403Type1 | ErrorMessage:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_0 = ErrorMessage.from_dict(data)

                return response_403_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_403_type_1 = ActionsRulesShowResponse403Type1.from_dict(data)

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
    ActionRuleDetailRead
    | ActionsRulesShowResponse403Type1
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
    action_rule: str,
    *,
    client: AuthenticatedClient,
    account_id: int | Unset = UNSET,
) -> Response[
    ActionRuleDetailRead
    | ActionsRulesShowResponse403Type1
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ValidationError
]:
    """Get an action rule

     Read the account-scoped rule, immutable revisions and recent run decisions. Send Accept:
    application/json for the documented JSON errors.

    Args:
        workspace (int):
        action_rule (str):
        account_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionRuleDetailRead | ActionsRulesShowResponse403Type1 | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        action_rule=action_rule,
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: int,
    action_rule: str,
    *,
    client: AuthenticatedClient,
    account_id: int | Unset = UNSET,
) -> (
    ActionRuleDetailRead
    | ActionsRulesShowResponse403Type1
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ValidationError
    | None
):
    """Get an action rule

     Read the account-scoped rule, immutable revisions and recent run decisions. Send Accept:
    application/json for the documented JSON errors.

    Args:
        workspace (int):
        action_rule (str):
        account_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionRuleDetailRead | ActionsRulesShowResponse403Type1 | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError
    """

    return sync_detailed(
        workspace=workspace,
        action_rule=action_rule,
        client=client,
        account_id=account_id,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    action_rule: str,
    *,
    client: AuthenticatedClient,
    account_id: int | Unset = UNSET,
) -> Response[
    ActionRuleDetailRead
    | ActionsRulesShowResponse403Type1
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ValidationError
]:
    """Get an action rule

     Read the account-scoped rule, immutable revisions and recent run decisions. Send Accept:
    application/json for the documented JSON errors.

    Args:
        workspace (int):
        action_rule (str):
        account_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionRuleDetailRead | ActionsRulesShowResponse403Type1 | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        action_rule=action_rule,
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    action_rule: str,
    *,
    client: AuthenticatedClient,
    account_id: int | Unset = UNSET,
) -> (
    ActionRuleDetailRead
    | ActionsRulesShowResponse403Type1
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ValidationError
    | None
):
    """Get an action rule

     Read the account-scoped rule, immutable revisions and recent run decisions. Send Accept:
    application/json for the documented JSON errors.

    Args:
        workspace (int):
        action_rule (str):
        account_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionRuleDetailRead | ActionsRulesShowResponse403Type1 | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            action_rule=action_rule,
            client=client,
            account_id=account_id,
        )
    ).parsed
