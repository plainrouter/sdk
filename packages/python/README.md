# Plainrouter Python SDK and CLI

Generated from Plainrouter's signed OpenAPI contract. The package is in 0.x and its API may change between minor releases. No support guarantees are made yet.

Official project: [plainrouter.com](https://plainrouter.com) · [documentation](https://plainrouter.com/docs/sdk/python) · [source](https://github.com/plainrouter/sdk/tree/main/packages/python)

Report Python SDK issues in the [Plainrouter SDK issue tracker](https://github.com/plainrouter/sdk/issues).

## Install

```bash
python -m pip install plainrouter
```

Python 3.11 or newer is required.

For command-line use, install the same package in an isolated environment:

```bash
pipx install plainrouter
plainrouter --help
```

You can also run the CLI from an active Python environment with
`python -m plainrouter`. The PyPI CLI provides the same command tree, config
path, environment variables, JSON output, and safety prompts as
[`@plainrouter/cli`](https://www.npmjs.com/package/@plainrouter/cli).

## Use

```python
from plainrouter import create_client, list_events

client = create_client("your-signal-tracker-secret")
response = list_events.sync(client=client)
```

Async operations are available through each operation module:

```python
from plainrouter import create_client, get_event

client = create_client("your-signal-tracker-secret")
response = await get_event.asyncio(event="event-id", client=client)
```

The default API base is `https://plainrouter.com/api/v1` and the default request timeout is 30 seconds. Pass `base_url` or an `httpx.Timeout` to `create_client` to override either setting. Credentials are supplied by the caller and are never embedded in the SDK.

Copy a failed plan to a fresh draft using a plan-writer bearer token:

```python
import os
from plainrouter import create_client, launch_plans_copy

client = create_client(os.environ["PLAINROUTER_TOKEN"])
response = launch_plans_copy.sync_detailed(1, "failed-plan-id", client=client)
```

The same operation provides `asyncio` and `asyncio_detailed` entry points. The
public `plainrouter.launch_plans_copy.PlanCopyResponse` type alias describes the
parsed result union, including `ProposalUnavailable` and `WorkspaceLockTimeout`.
The detailed entry points return `Response[PlanCopyResponse]`; `sync` and
`asyncio` return `PlanCopyResponse | None`.

## Retryable proposal errors

Pass the detailed response or raw HTTPX response to the helper, including for
async calls and endpoints with no documented 503. It recognizes only 503 error
envelopes with a string message and either `workspace_lock_timeout` or
`proposal_not_recorded`; other bodies return `False`.

```python
import json
from plainrouter import is_retryable_proposal_error

retryable = is_retryable_proposal_error(response.status_code, response)
error_code = json.loads(response.content)["error"]["code"] if retryable else None
retry_after = response.headers.get("Retry-After") if retryable else None
```

This example also distinguishes lock timeout (`error_code ==
"workspace_lock_timeout"`) without relying on `response.parsed`. If generated
parsing raises before returning a detailed response, capture the raw response
with an HTTPX response hook and call `response.read()` there; in an async hook,
await `response.aread()`. Run the same example on that captured response. Use
the public copy facade rather than calling generated copy directly.

No automatic retry is added. Honor `Retry-After` when present (delta seconds or
an HTTP date) when scheduling a retry.

Licensed under Apache-2.0.
