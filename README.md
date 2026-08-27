# PlainRouter SDK

Generated from PlainRouter's signed OpenAPI contract.

Official developer resources: [PlainRouter developer index](https://plainrouter.com/developers.md), [API documentation](https://plainrouter.com/docs/api-reference/introduction), and [OpenAPI specification](https://plainrouter.com/openapi.json).

Official project: [plainrouter.com](https://plainrouter.com) ·
[documentation](https://docs.plainrouter.com) ·
[source](https://github.com/plainrouter/sdk)

This repository is in `0.x` development. Stability and support are not yet
promised.

## TypeScript SDK

Install the generated SDK:

```sh
npm install @plainrouter/sdk
```

Inject a Signal Tracker secret explicitly, then call a generated operation:

```ts
import { configurePlainrouter, listEvents } from "@plainrouter/sdk";

configurePlainrouter({
  signalTrackerSecret: process.env.PLAINROUTER_TOKEN!,
});

const response = await listEvents();
```

The default API base URL is `https://plainrouter.com/api/v1`. The SDK never
embeds credentials.

## Python SDK

Install the Python SDK:

```sh
python -m pip install plainrouter
```

```python
from plainrouter import create_client, list_events

client = create_client("your-signal-tracker-secret")
response = list_events.sync(client=client)
```

Python 3.11 or newer is required. Python package releases are versioned
independently from the API contract and are verified against the vendored,
signed OpenAPI contract before publication.

## Ruby SDK

Install the Ruby gem:

```sh
gem install plainrouter-sdk
```

Use the compact client facade for the three API areas:

```ruby
require "plainrouter"

client = PlainRouter::Client.new(
  token: ENV.fetch("PLAINROUTER_TOKEN")
)

events = client.operations.list_events(per_page: 25)
```

Ruby 3.2 or newer is required. The complete generated models and HTTP-aware
methods remain available under `PlainRouter::OpenAPI` without crowding the
top-level SDK documentation.

## CLI

Install the canonical scoped CLI globally:

```sh
npm i -g @plainrouter/cli
plainrouter --help
```

Or run the scoped package without installing it globally:

```sh
npx @plainrouter/cli --help
```

Python users can install the equivalent CLI from
[PyPI](https://pypi.org/project/plainrouter/) with `pipx`:

```sh
pipx install plainrouter
plainrouter --help
```

Both distributions expose the `plainrouter` command. Keep only one global
installation on your `PATH` to avoid selecting an unintended executable.

Provide a Signal Tracker secret without placing it in shell history:

```sh
read -s PLAINROUTER_TOKEN
export PLAINROUTER_TOKEN
plainrouter events list
unset PLAINROUTER_TOKEN
```

The same CLI is also available from the official Homebrew tap:

```sh
brew install plainrouter/tap/plainrouter
```

## Go SDK

The generated Go client is published as its own standard Go module:

```sh
go get github.com/plainrouter/sdk-go@v0.5.0
```

## AI agents

This is PlainRouter's public repository for agent integrations and generated SDKs. It includes:

- repository guidance for Claude Code, Codex, Cursor, and Windsurf;
- Agent Plugin manifests for Claude Code and Codex;
- a Streamable HTTP MCP configuration for `https://plainrouter.com/mcp`; and
- three official Agent Skills:
  - [`get-ad-account-context`](skills/get-ad-account-context/SKILL.md) for approved account context and read-only measurements;
  - [`verify-signal-ingestion`](skills/verify-signal-ingestion/SKILL.md) for an idempotent identity-free onboarding check; and
  - [`propose-governed-ad-actions`](skills/propose-governed-ad-actions/SKILL.md) for evidence-backed proposals subject to policy and human approval.

Install the skills with the open Agent Skills CLI:

```sh
npx skills add plainrouter/sdk
```

The MCP server uses OAuth 2.1 with the `mcp:use` scope. Review [authentication](https://plainrouter.com/auth.md) before connecting an agent. Account access remains limited to the advertising account approved by the human user.
