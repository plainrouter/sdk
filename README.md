# Plainrouter: Meta Ads MCP server, SDKs and CLI

<!-- mcp-name: com.plainrouter/mcp -->

**Plainrouter is a hosted Meta Ads MCP server and API for developers and AI agents.** Connect Claude, ChatGPT, Codex, Cursor, Gemini CLI or another MCP client to read a Meta ad account and its conversion-signal health. The agent can then propose pauses, resumes, budget changes and creative tests. Workspace policy checks every proposal. In Ask mode a person approves each change; in Full mode policy-allowed changes run automatically. New ad copies are created paused.

Plainrouter also keeps its own count of website arrivals and verified revenue beside Meta's reported numbers, so an agent can check Meta's claims against independent evidence.

This repository holds Plainrouter's public SDKs (TypeScript, Python, Ruby and PHP; Go lives in [plainrouter/sdk-go](https://github.com/plainrouter/sdk-go)), the CLI, MCP metadata and official Agent Skills.

## At a glance

| | |
| --- | --- |
| MCP endpoint | `https://plainrouter.com/mcp` (Streamable HTTP) |
| Sandbox | `https://plainrouter.com/mcp/sandbox`: no account or credential, synthetic data, never contacts Meta |
| Authentication | A Workspace key sent as a bearer token, or Plainrouter OAuth sign-in where the client supports it |
| Access tiers | **Read** for account, signal, inventory and creative reads; **Write** adds previews and proposals |
| Approvals | **Ask**: a person approves each change. **Full**: policy-allowed changes run automatically. Rule violations are blocked, the kill switch stops further writes, and every change gets a decision receipt |
| Clients | Claude Code, Claude, ChatGPT (developer mode), Codex, Cursor, Gemini CLI, Grok, Meta Muse, Hermes, OpenClaw, n8n and Make ([setup guides](https://plainrouter.com/docs/mcp/clients)) |
| Pricing | MCP is included on every plan and calls are not metered. Free below €300 of monthly ad spend ([pricing](https://plainrouter.com/pricing)) |
| Registry | `com.plainrouter/mcp` in the [official MCP Registry](https://registry.modelcontextprotocol.io) |
| Docs | [MCP overview](https://plainrouter.com/docs/mcp/overview) · [Meta Ads MCP server](https://plainrouter.com/solutions/meta-ads-mcp) |

## Quick start

### 1. Try the sandbox, no account needed

Claude Code:

```sh
claude mcp add --transport http plainrouter-test https://plainrouter.com/mcp/sandbox
```

Codex (`~/.codex/config.toml`):

```toml
[mcp_servers.plainrouter-test]
url = "https://plainrouter.com/mcp/sandbox"
```

Ask the agent to call `get_account_state`, then `get_signal_health`. Every response is synthetic and marked `"sandbox": true`.

### 2. Connect your Meta ad account

Create a Workspace key in **Settings → Workspace keys** (start with **Read**), keep it in an environment variable, and point your client at `https://plainrouter.com/mcp`.

Claude Code (`.mcp.json`):

```json
{
  "mcpServers": {
    "plainrouter": {
      "type": "http",
      "url": "https://plainrouter.com/mcp",
      "headers": { "Authorization": "Bearer ${PLAINROUTER_WORKSPACE_TOKEN}" }
    }
  }
}
```

Codex (`~/.codex/config.toml`):

```toml
[mcp_servers.plainrouter]
url = "https://plainrouter.com/mcp"
bearer_token_env_var = "PLAINROUTER_WORKSPACE_TOKEN"
```

ChatGPT (developer mode), Claude custom connectors and Cursor can sign in with OAuth instead. Add `https://plainrouter.com/mcp`, then choose the Meta ad account and Read or Write access on Plainrouter's consent screen. Never put a credential in the endpoint URL or in a prompt.

Call `get_account_state` first and confirm the workspace and Meta ad account before any other work. Other clients: [setup guides](https://plainrouter.com/docs/mcp/clients).

## FAQ

### What is a Meta Ads MCP server?

A Model Context Protocol server that exposes a Meta ad account as tools an AI client can call. Plainrouter's is hosted, so there is nothing to install or keep a Meta token for. It adds conversion-signal diagnostics, one-workspace keys and an approval step for supported changes.

### Can an AI agent analyze my Meta ads without changing anything?

Yes. A Read key covers account, Signals, inventory and creative-library reads and cannot preview or propose changes. It can still submit feedback and run the optional ingestion diagnostic, which writes one identity-free test event.

### How is this different from Meta's own Ads MCP server?

Meta hosts a first-party server at `https://mcp.facebook.com/ads` for its own advertising operations, and it is the first option to evaluate for direct access. Plainrouter adds an independent conversion count and delivery diagnostics, Ask/Full approvals with policy checks and receipts, and keys scoped to one workspace. See the [Meta Ads MCP comparison](https://plainrouter.com/library/meta-ads-mcp-options).

### Does it work with ChatGPT?

Yes, in ChatGPT developer mode on paid plans. Add `https://plainrouter.com/mcp` with OAuth and choose the ad account on Plainrouter's consent screen. The sandbox works there with No Authentication.

### What does it cost?

MCP is included on every Plainrouter plan, and MCP calls are not metered. Plainrouter is free below €300 of observed monthly ad spend.

## Agent Skills

For agents, the repository also includes:

- repository guidance for Claude Code, Codex, Cursor, and Windsurf;
- Agent Plugin manifests for Claude Code and Codex;
- a Streamable HTTP MCP configuration for `https://plainrouter.com/mcp`; and
- three official Agent Skills:
  - [`get-ad-account-context`](skills/get-ad-account-context/SKILL.md) for approved account context and read-only measurements;
  - [`verify-signal-ingestion`](skills/verify-signal-ingestion/SKILL.md) for an idempotent identity-free onboarding check; and
  - [`propose-governed-ad-actions`](skills/propose-governed-ad-actions/SKILL.md) for evidence-backed proposals governed by Ask or Full.

Install the skills with the open Agent Skills CLI:

```sh
npx skills add plainrouter/sdk
```

## Tools

The live server advertises 32 tools. Your key tier, grants and the selected ad account decide which ones a connection can use. The full contracts are in the [MCP tool reference](https://plainrouter.com/docs/mcp/tools).

| Tool | Kind | What it does |
| --- | --- | --- |
| **Account and reporting** | | |
| `get_account_state` | Read | Return the authorized advertising account, workspace, connection, Signal destination, and currently available account capabilities. |
| `get_account_inventory` | Read | Read the authorized workspace account inventory from the Meta mirror, with optional level, status, parent, and ID cursor filters. |
| `get_inventory_metrics` | Read | Read daily Meta metrics beside counted Plainrouter arrivals for mirrored campaigns, ad sets and ads. |
| `get_performance` | Read | Compare Meta-reported conversions with the conversions Plainrouter accepted and verified for the selected account. |
| `get_arrivals_comparison` | Read | Return counted arrivals beside Meta outbound clicks for the authorized workspace and selected trailing window. |
| `get-creative-library` | Read | Return Meta image and video assets with the ads and last-30-day performance historically associated with each asset. |
| **Conversion signals** | | |
| `get_signal_health` | Read | Diagnostic view of first-party event flow, Meta delivery outcomes, match quality, and reconciliation gaps from Plainrouter stored measurements. |
| `get_install_instructions` | Read | Return managed-hostname Path A installation material and first-arrival state for the authorized workspace. |
| `verify_signal_ingestion` | Write | Verify server-side Signal ingestion by writing one idempotent, identity-free modeled event for the authorized workspace. |
| **Actions (governed changes)** | | |
| `dry_run_actions` | Read | Preview policy decisions and execution diffs for a proposed Action batch without writing it. |
| `propose-actions` | Write | Propose a batch of budget, status, upload, or creative-duplication actions for the approved ad account. |
| `upload-asset` | Write | Stage a JPEG/PNG image and submit a canonical upload action through workspace policy. |
| `duplicate-ad-with-creative` | Write | Submit a canonical proposal to duplicate a source Meta ad with a different creative asset. |
| `list_actions` | Read | List proposed actions for the authorized workspace and advertising account. |
| `get_action_batch` | Read | Get a proposed action batch for the authorized workspace and advertising account. |
| `get_action` | Read | Get one proposed action for the authorized workspace and advertising account. |
| `get_action_decision_receipt` | Read | Get the persisted decision receipt for an authorized proposed action. |
| `get_action_policy` | Read | Get the effective Actions policy for the authorized workspace without creating a policy row. |
| **Launch** | | |
| `launch.creatives.index` | Read | List creatives in the workspace bound to the authenticated execution token. |
| `launch.creatives.show` | Read | Show one creative in the workspace bound to the authenticated execution token. |
| `launch.creatives.store` | Write | Store one JPEG, PNG, MP4, or QuickTime creative from strict base64 content in the token-bound workspace. |
| `launch.creatives.store-from-url` | Write | Fetch and store one creative from a vetted HTTPS URL in the token-bound workspace. |
| `launch.creatives.status` | Write | Set the status of one creative in the workspace bound to the authenticated execution token. |
| `launch.plans.list` | Read | List deployment plans for the approved ad account, including each current review_version to pass when executing the reviewed plan. |
| `launch.plans.show` | Read | Read one deployment plan and its current review_version and latest launch-intent status in the workspace and ad account bound to the execution token. |
| `launch.plans.create` | Write | Create a deployment plan for the approved ad account. |
| `launch.plans.update` | Write | Update a deployment plan for the approved ad account. |
| `launch.plans.validate` | Write | Validate a deployment plan for the approved ad account. |
| `launch.plans.copy` | Write | Copy a failed plan to a new draft with the same content. |
| `launch.plans.execute` | Write | Execute one deployment plan in the workspace and ad account bound to the execution token; requires the review_version returned by the plan read you acted on. |
| **Workspace** | | |
| `revoke_grant` | Write | Revoke an active workspace grant. |
| `submit_feedback` | Write | Report a bug or a missing capability you hit while using this server. |

Every change to Meta goes through Actions: policy checks, the workspace's Ask or Full mode, provider verification and a decision receipt.

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

## Action policy compatibility

The next npm and Python version is `0.7.0`; the next Ruby version is `0.3.0`.
These breaking `0.x` updates remove retired workspace policy settings from the
generated clients. Policy reads expose execution mode and outcome-check settings.
Update integrations to consume the current signed policy response.

In Ask mode, a person approves every change first. In Full mode, the workspace
lets changes run automatically without a per-change approval. Every change gets
a receipt, and the kill switch stops all changes. It does not undo earlier changes.

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

## PHP SDK

Install the PHP package:

```sh
composer require plainrouter/sdk
```

Use the compact client facade for the three API areas:

```php
use Plainrouter\Client;

$client = new Client(token: getenv('PLAINROUTER_TOKEN'));

$events = $client->operations->listEvents(25);
```

PHP 8.2 or newer is required. The complete generated models and HTTP-aware
methods remain available under `Plainrouter\OpenAPI`.

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

Official developer resources: [documentation](https://plainrouter.com/docs), [API documentation](https://plainrouter.com/docs/api/introduction), and [OpenAPI specification](https://plainrouter.com/openapi.json).

Official project: [plainrouter.com](https://plainrouter.com) ·
[documentation](https://plainrouter.com/docs) ·
[source](https://github.com/plainrouter/sdk)

This repository is in `0.x` development. Stability and support are not yet
promised.
