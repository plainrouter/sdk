---
name: verify-signal-ingestion
description: Verify end-to-end server-side Signal ingestion through PlainRouter with one idempotent identity-free event. Use for Signal onboarding verification; use get_signal_health instead for read-only diagnostics.
---

# Verify Signal Ingestion

Use this skill when a human asks to verify that a newly installed PlainRouter Signal can accept a server-side event. The verification writes one identity-free test event and confirms its receipt in the Signal ledger; it has no advertising-spend capability.

## Connect

1. Connect to the Streamable HTTP MCP endpoint at `https://plainrouter.com/mcp`.
2. Follow the OAuth 2.1 flow documented at `https://plainrouter.com/auth.md`.
3. Request only the `mcp:use` scope and let the human choose an advertising account.

## Verify ingestion

Call `get_account_state` first. Confirm that the authorized workspace has an active Signal and that the connection permissions include `signals.verify`.

If the user only wants a read-only diagnosis, call `get_signal_health` and do not create a verification event. When the user explicitly asks to test or verify ingestion, call `verify_signal_ingestion` with no arguments.

Report success only when the tool confirms ledger receipt. If it reports a missing authorization, workspace, or active Signal, return that prerequisite without retrying against another account. Repeating the same verification is idempotent, but do not loop retries after a persistent failure.

## Boundaries

The verification event contains no customer identity or conversion value. It proves PlainRouter ingestion and ledger receipt only. It does not prove downstream ad-platform delivery, attribution, campaign access, or permission to spend.

For endpoint schemas or direct API integration, use the signed OpenAPI specification at `https://plainrouter.com/openapi.json` and the developer index at `https://plainrouter.com/developers.md`.
