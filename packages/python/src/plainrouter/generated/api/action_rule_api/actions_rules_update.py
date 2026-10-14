from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_rule_write_read import ActionRuleWriteRead
from ...models.actions_rules_update_body import ActionsRulesUpdateBody
from ...models.actions_rules_update_response_403_type_1 import ActionsRulesUpdateResponse403Type1
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.error_message import ErrorMessage
from ...models.validation_error import ValidationError
from ...models.workspace_lock_timeout import WorkspaceLockTimeout
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: int,
    action_rule: str,
    *,
    body: ActionsRulesUpdateBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/agent/workspaces/{workspace}/action-rules/{action_rule}".format(
            workspace=quote(str(workspace), safe=""),
            action_rule=quote(str(action_rule), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ActionRuleWriteRead
    | ActionsRulesUpdateResponse403Type1
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ValidationError
    | WorkspaceLockTimeout
    | None
):
    if response.status_code == 200:
        response_200 = ActionRuleWriteRead.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

    if response.status_code == 403:

        def _parse_response_403(data: object) -> ActionsRulesUpdateResponse403Type1 | ErrorMessage:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_0 = ErrorMessage.from_dict(data)

                return response_403_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_403_type_1 = ActionsRulesUpdateResponse403Type1.from_dict(data)

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

    if response.status_code == 503:
        response_503 = WorkspaceLockTimeout.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ActionRuleWriteRead
    | ActionsRulesUpdateResponse403Type1
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ValidationError
    | WorkspaceLockTimeout
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
    body: ActionsRulesUpdateBody | Unset = UNSET,
) -> Response[
    ActionRuleWriteRead
    | ActionsRulesUpdateResponse403Type1
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ValidationError
    | WorkspaceLockTimeout
]:
    """Update an action rule

     Write an account-scoped rule using its validated definition. Send Accept: application/json for JSON
    errors. New rules start disabled.

    Args:
        workspace (int):
        action_rule (str):
        body (ActionsRulesUpdateBody | Unset): All fields are optional. platform_ad_account_id
            must be absent. window, window_days, author_type and current_revision_id must be absent or
            empty.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionRuleWriteRead | ActionsRulesUpdateResponse403Type1 | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError | WorkspaceLockTimeout]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        action_rule=action_rule,
        body=body,
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
    body: ActionsRulesUpdateBody | Unset = UNSET,
) -> (
    ActionRuleWriteRead
    | ActionsRulesUpdateResponse403Type1
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ValidationError
    | WorkspaceLockTimeout
    | None
):
    """Update an action rule

     Write an account-scoped rule using its validated definition. Send Accept: application/json for JSON
    errors. New rules start disabled.

    Args:
        workspace (int):
        action_rule (str):
        body (ActionsRulesUpdateBody | Unset): All fields are optional. platform_ad_account_id
            must be absent. window, window_days, author_type and current_revision_id must be absent or
            empty.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionRuleWriteRead | ActionsRulesUpdateResponse403Type1 | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError | WorkspaceLockTimeout
    """

    return sync_detailed(
        workspace=workspace,
        action_rule=action_rule,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    action_rule: str,
    *,
    client: AuthenticatedClient,
    body: ActionsRulesUpdateBody | Unset = UNSET,
) -> Response[
    ActionRuleWriteRead
    | ActionsRulesUpdateResponse403Type1
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ValidationError
    | WorkspaceLockTimeout
]:
    """Update an action rule

     Write an account-scoped rule using its validated definition. Send Accept: application/json for JSON
    errors. New rules start disabled.

    Args:
        workspace (int):
        action_rule (str):
        body (ActionsRulesUpdateBody | Unset): All fields are optional. platform_ad_account_id
            must be absent. window, window_days, author_type and current_revision_id must be absent or
            empty.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionRuleWriteRead | ActionsRulesUpdateResponse403Type1 | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError | WorkspaceLockTimeout]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        action_rule=action_rule,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    action_rule: str,
    *,
    client: AuthenticatedClient,
    body: ActionsRulesUpdateBody | Unset = UNSET,
) -> (
    ActionRuleWriteRead
    | ActionsRulesUpdateResponse403Type1
    | ErrorMessage
    | ApiRouteNotFound
    | ErrorMessage
    | ValidationError
    | WorkspaceLockTimeout
    | None
):
    """Update an action rule

     Write an account-scoped rule using its validated definition. Send Accept: application/json for JSON
    errors. New rules start disabled.

    Args:
        workspace (int):
        action_rule (str):
        body (ActionsRulesUpdateBody | Unset): All fields are optional. platform_ad_account_id
            must be absent. window, window_days, author_type and current_revision_id must be absent or
            empty.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionRuleWriteRead | ActionsRulesUpdateResponse403Type1 | ErrorMessage | ApiRouteNotFound | ErrorMessage | ValidationError | WorkspaceLockTimeout
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            action_rule=action_rule,
            client=client,
            body=body,
        )
    ).parsed
