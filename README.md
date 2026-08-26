# PlainRouter SDK

Generated from PlainRouter's signed OpenAPI contract.

Official developer resources: [PlainRouter developer index](https://plainrouter.com/developers.md), [API documentation](https://plainrouter.com/docs/api-reference/introduction), and [OpenAPI specification](https://plainrouter.com/openapi.json).

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

Python 3.11 or newer is required. The package version stays aligned with the
signed OpenAPI contract.

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

Provide a Signal Tracker secret without placing it in shell history:

```sh
read -s PLAINROUTER_TOKEN
export PLAINROUTER_TOKEN
plainrouter events list
unset PLAINROUTER_TOKEN
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
npx skills add wudaku/plainrouter-sdk
```

The MCP server uses OAuth 2.1 with the `mcp:use` scope. Review [authentication](https://plainrouter.com/auth.md) before connecting an agent. Account access remains limited to the advertising account approved by the human user.
