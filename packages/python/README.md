# PlainRouter Python SDK and CLI

Generated from Plainrouter's signed OpenAPI contract. The package is in 0.x and its API may change between minor releases. No support guarantees are made yet.

Official project: [plainrouter.com](https://plainrouter.com) · [documentation](https://plainrouter.com/developers.md) · [source](https://github.com/plainrouter/sdk/tree/main/packages/python)

Report Python SDK issues in the [PlainRouter SDK issue tracker](https://github.com/plainrouter/sdk/issues).

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

Licensed under Apache-2.0.
