from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_route_not_found import ApiRouteNotFound
from ...models.error_message import ErrorMessage
from ...models.launch_plans_update_response_200 import LaunchPlansUpdateResponse200
from ...models.update_deployment_plan_request import UpdateDeploymentPlanRequest
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: int,
    deployment_plan: str,
    *,
    body: UpdateDeploymentPlanRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/workspaces/{workspace}/admin/plans/{deployment_plan}".format(
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
) -> ApiRouteNotFound | ErrorMessage | LaunchPlansUpdateResponse200 | ValidationError | None:
    if response.status_code == 200:
        response_200 = LaunchPlansUpdateResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiRouteNotFound.from_dict(response.json())

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
) -> Response[ApiRouteNotFound | ErrorMessage | LaunchPlansUpdateResponse200 | ValidationError]:
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
    client: AuthenticatedClient | Client,
    body: UpdateDeploymentPlanRequest | Unset = UNSET,
) -> Response[ApiRouteNotFound | ErrorMessage | LaunchPlansUpdateResponse200 | ValidationError]:
    """Update a deployment plan

     Create or edit a draft deployment plan for the authorized advertising account. Review and validate
    the plan before submitting any provider writes.

    Args:
        workspace (int):
        deployment_plan (str):
        body (UpdateDeploymentPlanRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | ErrorMessage | LaunchPlansUpdateResponse200 | ValidationError]
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
    client: AuthenticatedClient | Client,
    body: UpdateDeploymentPlanRequest | Unset = UNSET,
) -> ApiRouteNotFound | ErrorMessage | LaunchPlansUpdateResponse200 | ValidationError | None:
    """Update a deployment plan

     Create or edit a draft deployment plan for the authorized advertising account. Review and validate
    the plan before submitting any provider writes.

    Args:
        workspace (int):
        deployment_plan (str):
        body (UpdateDeploymentPlanRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | ErrorMessage | LaunchPlansUpdateResponse200 | ValidationError
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
    client: AuthenticatedClient | Client,
    body: UpdateDeploymentPlanRequest | Unset = UNSET,
) -> Response[ApiRouteNotFound | ErrorMessage | LaunchPlansUpdateResponse200 | ValidationError]:
    """Update a deployment plan

     Create or edit a draft deployment plan for the authorized advertising account. Review and validate
    the plan before submitting any provider writes.

    Args:
        workspace (int):
        deployment_plan (str):
        body (UpdateDeploymentPlanRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRouteNotFound | ErrorMessage | LaunchPlansUpdateResponse200 | ValidationError]
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
    client: AuthenticatedClient | Client,
    body: UpdateDeploymentPlanRequest | Unset = UNSET,
) -> ApiRouteNotFound | ErrorMessage | LaunchPlansUpdateResponse200 | ValidationError | None:
    """Update a deployment plan

     Create or edit a draft deployment plan for the authorized advertising account. Review and validate
    the plan before submitting any provider writes.

    Args:
        workspace (int):
        deployment_plan (str):
        body (UpdateDeploymentPlanRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRouteNotFound | ErrorMessage | LaunchPlansUpdateResponse200 | ValidationError
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            deployment_plan=deployment_plan,
            client=client,
            body=body,
        )
    ).parsed
