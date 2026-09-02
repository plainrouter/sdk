---
name: get-ad-account-context
description: Read an approved advertising account's identity, first-party signal health, and verified performance through PlainRouter. Use for account-specific advertising analysis through the PlainRouter MCP server; do not use it to claim direct campaign mutation access.
---

# PlainRouter Ad Context

Use this skill before performing account-specific work through PlainRouter. It identifies the single advertising account the human approved for the current connection.

## Connect

1. Connect to the Streamable HTTP MCP endpoint at `https://plainrouter.com/mcp`.
2. Follow the OAuth 2.1 flow documented at `https://plainrouter.com/auth.md`.
3. Request only the `mcp:use` scope and let the human choose an advertising account.

## Read account and signal state

Call `get_account_state` before relying on account-specific assumptions. Use its response as the authority for:

- the connection identity and granted permissions;
- the approved advertising account ID and name;
- platform, currency, timezone, and owning workspace;
- whether first-party Signals and a Meta dataset are connected; and
- the read-only capabilities available to the connection.

Call `get_signal_health` when asked whether tracking is healthy, match quality is changing, or deliveries need attention. Its answer comes from PlainRouter's retained event and delivery ledgers, stored EMQ snapshots, and stored reconciliation reports. Do not describe it as a live Marketing API request.

Call `get_performance` to compare Meta-reported conversions with gateway-verified accepted conversions. Pass `days` from 1 to 90; the default is 7.

## Boundaries

Treat the returned context as read-only. Never infer access to another advertising account or claim direct campaign mutation.

When `actions.propose` is present, changes may only be submitted through `propose-actions`. PlainRouter workspace policy and every required human approval remain authoritative. Describe a proposal as proposed, not applied, until the tool result proves otherwise.

For endpoint schemas or direct API integration, use the signed OpenAPI specification at `https://plainrouter.com/openapi.json` and the Conversion API documentation at `https://plainrouter.com/docs/reference/conversion-api`.
