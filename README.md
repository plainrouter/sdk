# PlainRouter SDK

<!-- mcp-name: com.plainrouter/plainrouter -->

PlainRouter is an independent arrival ledger and spend enforcement under the ad account. Agents can trust its reads because the platform being measured does not produce them, and its enforcement is structural, not advisory.

## Connect to PlainRouter MCP

PlainRouter exposes a remote Streamable HTTP MCP server at [https://plainrouter.com/mcp](https://plainrouter.com/mcp).

The server uses OAuth 2.1. Request only the `mcp:use` scope. Account access is limited to the advertising account approved by the human user. Complete OAuth authorization in your client's normal flow; do not place credentials in the endpoint URL. Review [authentication](https://plainrouter.com/docs/auth) before connecting an agent.

### Claude (integrations UI)

In Claude's Integrations UI, add a remote MCP server and enter `https://plainrouter.com/mcp`. Complete the OAuth 2.1 authorization and approve only the human-selected advertising account.

### Cursor (`mcp.json`)

Add the remote server to Cursor's `mcp.json`:

```json
{
  "mcpServers": {
    "plainrouter": {
      "url": "https://plainrouter.com/mcp"
    }
  }
}
```

When Cursor prompts you, complete OAuth 2.1 and grant only `mcp:use`; the connection can access only the advertising account approved by the human.

### Generic Streamable HTTP client

Configure the client's Streamable HTTP transport with endpoint `https://plainrouter.com/mcp`. Use its OAuth 2.1 flow to request only `mcp:use`, and send the resulting authorization through the client's standard HTTP authentication mechanism. Account access remains limited to the human-approved advertising account.

## Agent Skills

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

## Tools

The live MCP server advertises these tools. Availability remains limited by the connection permissions and the human-approved advertising account.

| Tool | Description and agent-facing constraint |
| --- | --- |
| `get_account_state` | Reads the authorized account, workspace, connection, Signal destination, and available read-only capabilities. Read-only and idempotent; use it before account-specific work. |
| `get_signal_health` | Diagnoses stored event flow, Meta delivery outcomes, match quality, and reconciliation gaps. Read-only and idempotent; it does not call the Marketing API and is not evidence for spend-affecting proposals. |
| `get_performance` | Returns admissible proposal evidence comparing Meta-reported conversions with gateway-verified accepted conversions. Read-only and idempotent; `days` accepts 1–90 and defaults to 7. |
| `verify_signal_ingestion` | Writes one identity-free onboarding verification event and confirms ledger receipt. Idempotent and has no spend capability. |
| `propose-actions` | Proposes 1–25 budget, status, upload, or creative-duplication actions. Idempotent; every proposal passes workspace policy, and suggest-only approval never executes it. |
| `get-creative-library` | Reads Meta image and video assets, historically associated ads, and 30-day performance. Read-only; results can be filtered and paginated. |
| `upload-asset` | Stages a JPEG or PNG image and submits a canonical upload action. Idempotent and non-destructive; the action remains policy- and approval-gated. |
| `duplicate-ad-with-creative` | Proposes duplicating a source Meta ad with a selected creative asset. Idempotent and non-destructive; approved copies are always created paused. |
| `launcher.draft_batch` | Creates a Launch draft from already-synced Drive assets in the execution token's workspace and ad account. Creates draft state only and accepts no caller-supplied account context. |
| `launcher.batch_status` | Reads the bounded status projection of a token-bound Launch batch. Read-only and idempotent. |
| `launcher.preview_batch` | Runs the authoritative Launch gate preview checkpoint for a token-bound batch. Non-destructive; a blocked gate prevents advancement. |
| `launcher.execute_batch` | Enters execution for a token-bound Launch batch. Every mutation is proposed through Actions rather than applied outside the governed lane. |
| `show_spend_cap_approval` | Renders the static spend-cap approval preview card. Read-only and idempotent; it reads and writes nothing. |

Generated from PlainRouter's signed OpenAPI contract.

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

## Go SDK

The generated Go client is published as its own standard Go module:

```sh
go get github.com/plainrouter/sdk-go@v0.5.0
```

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

## Developer resources

Official developer resources: [PlainRouter developer index](https://plainrouter.com/developers.md), [API documentation](https://plainrouter.com/docs/reference/conversion-api), and [OpenAPI specification](https://plainrouter.com/openapi.json).

Official project: [plainrouter.com](https://plainrouter.com) ·
[documentation](https://plainrouter.com/docs) ·
[source](https://github.com/plainrouter/sdk)

This repository is in `0.x` development. Stability and support are not yet
promised.
