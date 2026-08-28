---
name: propose-governed-ad-actions
description: Prepare evidence-backed advertising action proposals through PlainRouter. Use for human-requested budget, status, asset, or creative changes; never describe a proposal as applied.
---

# Propose Governed Ad Actions

Use this skill when a human asks to prepare a budget, status, asset-upload, or creative-duplication proposal for the one advertising account approved through PlainRouter. A proposal is not an applied campaign change.

## Connect

1. Connect to the Streamable HTTP MCP endpoint at `https://plainrouter.com/mcp`.
2. Follow the OAuth 2.1 flow documented at `https://plainrouter.com/docs/auth`.
3. Request only the `mcp:use` scope and let the human choose an advertising account.

## Prepare evidence

Call `get_account_state` first. Stop if `actions.propose` is absent. Asset-upload and creative-duplication proposals also require `creative.write`.

The human must supply the platform-native target ID. Never infer a campaign, ad set, or ad target from unrelated account data.

For spend-affecting proposals, call `get_performance` with the shortest useful window from 1 to 90 days. Cite only exact returned field paths. `get_signal_health` is diagnostic and is not admissible evidence for spend-affecting proposals. If `measurability.quantitative_citations_allowed` is false, do not cite quantitative performance fields.

## Submit the proposal

Call `propose-actions` with:

- one to twenty-five supported action objects;
- a plain-language batch rationale;
- a stable idempotency key of at most 64 characters;
- one to three exact evidence declarations; and
- `target_source` set to `human_supplied`.

Supported actions are budget adjustment, status change, asset upload, and creative duplication. Creative duplication must create the new ad paused.

## Boundaries

Describe the outcome using the tool's actual status. Workspace policy may reject the proposal or place it in a human approval queue. Never describe a proposal as approved, executed, or reflected on an ad platform unless a later authoritative result proves that state. No ad-activation action is exposed.

For the complete payload schema, use the tool definition returned by the MCP server. For direct API integration, use `https://plainrouter.com/openapi.json` and `https://plainrouter.com/developers.md`.
