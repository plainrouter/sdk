from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.error_message import ErrorMessage
from ...models.execute_deployment_plan_request import ExecuteDeploymentPlanRequest
from ...models.launch_intent_read import LaunchIntentRead
from ...models.plan_execute_conflict import PlanExecuteConflict
from ...models.plan_execute_rejected import PlanExecuteRejected
from ...models.validation_error import ValidationError
from ...models.workspace_lock_timeout import WorkspaceLockTimeout
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: int,
    deployment_plan: str,
    *,
    body: ExecuteDeploymentPlanRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workspaces/{workspace}/admin/plans/{deployment_plan}/execute".format(
            workspace=quote(str(workspace), safe=""),
            deployment_plan=quote(str(deployment_plan), safe=""),
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
    ApiRouteNotFound
    | ErrorMessage
    | LaunchIntentRead
    | PlanExecuteConflict
    | PlanExecuteRejected
    | ValidationError
    | WorkspaceLockTimeout
    | None
):
    if response.status_code == 200:
        response_200 = LaunchIntentRead.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorMessage.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiRouteNotFound.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = PlanExecuteConflict.from_dict(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = ErrorMessage.from_dict(response.json())

        return response_413

    if response.status_code == 422:

        def _parse_response_422(data: object) -> PlanExecuteRejected | ValidationError:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = ValidationError.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_1 = PlanExecuteRejected.from_dict(data)

            return response_422_type_1

        response_422 = _parse_response_422(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ErrorMessage.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorMessage.from_dict(response.json())

        return response_500

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
    ApiRouteNotFound
    | ErrorMessage
    | LaunchIntentRead
    | PlanExecuteConflict
    | PlanExecuteRejected
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
    deployment_plan: str,
    *,
    client: AuthenticatedClient,
    body: ExecuteDeploymentPlanRequest | Unset = UNSET,
) -> Response[
    ApiRouteNotFound
    | ErrorMessage
    | LaunchIntentRead
    | PlanExecuteConflict
    | PlanExecuteRejected
    | ValidationError
    | WorkspaceLockTimeout
]:
    """Execute a deployment plan

     Create or replay a governed Launch intent for the approved account. A kill switch returns a blocked
    intent without executing provider writes.

    Args:
        workspace (int):
        deployment_plan (str):
        body (ExecuteDeploymentPlanRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | ErrorMessage | LaunchIntentRead | PlanExecuteConflict | PlanExecuteRejected | ValidationError | WorkspaceLockTimeout]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        deployment_plan=deployment_plan,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: int,
    deployment_plan: str,
    *,
    client: AuthenticatedClient,
    body: ExecuteDeploymentPlanRequest | Unset = UNSET,
) -> (
    ApiRouteNotFound
    | ErrorMessage
    | LaunchIntentRead
    | PlanExecuteConflict
    | PlanExecuteRejected
    | ValidationError
    | WorkspaceLockTimeout
    | None
):
    """Execute a deployment plan

     Create or replay a governed Launch intent for the approved account. A kill switch returns a blocked
    intent without executing provider writes.

    Args:
        workspace (int):
        deployment_plan (str):
        body (ExecuteDeploymentPlanRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | ErrorMessage | LaunchIntentRead | PlanExecuteConflict | PlanExecuteRejected | ValidationError | WorkspaceLockTimeout
    """

    return sync_detailed(
        workspace=workspace,
        deployment_plan=deployment_plan,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace: int,
    deployment_plan: str,
    *,
    client: AuthenticatedClient,
    body: ExecuteDeploymentPlanRequest | Unset = UNSET,
) -> Response[
    ApiRouteNotFound
    | ErrorMessage
    | LaunchIntentRead
    | PlanExecuteConflict
    | PlanExecuteRejected
    | ValidationError
    | WorkspaceLockTimeout
]:
    """Execute a deployment plan

     Create or replay a governed Launch intent for the approved account. A kill switch returns a blocked
    intent without executing provider writes.

    Args:
        workspace (int):
        deployment_plan (str):
        body (ExecuteDeploymentPlanRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | ErrorMessage | LaunchIntentRead | PlanExecuteConflict | PlanExecuteRejected | ValidationError | WorkspaceLockTimeout]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        deployment_plan=deployment_plan,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: int,
    deployment_plan: str,
    *,
    client: AuthenticatedClient,
    body: ExecuteDeploymentPlanRequest | Unset = UNSET,
) -> (
    ApiRouteNotFound
    | ErrorMessage
    | LaunchIntentRead
    | PlanExecuteConflict
    | PlanExecuteRejected
    | ValidationError
    | WorkspaceLockTimeout
    | None
):
    """Execute a deployment plan

     Create or replay a governed Launch intent for the approved account. A kill switch returns a blocked
    intent without executing provider writes.

    Args:
        workspace (int):
        deployment_plan (str):
        body (ExecuteDeploymentPlanRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | ErrorMessage | LaunchIntentRead | PlanExecuteConflict | PlanExecuteRejected | ValidationError | WorkspaceLockTimeout
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            deployment_plan=deployment_plan,
            client=client,
            body=body,
        )
    ).parsed
