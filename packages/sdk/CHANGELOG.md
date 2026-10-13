# Changelog

## 0.10.0 (unreleased)

- Normalize header names case-insensitively for object, Headers, tuple and array-value request options before generated merging; caller values replace defaults. On the 13 operations that send a body, a per-call `Headers` instance or tuple array is not applied, as on main; a plain object works on every operation.

- Export `ApiRedirectError` (response/status/headers) and the optional `PlainrouterConfig.headers` configuration field for caller overrides.

- Default to `Accept: application/json` (caller headers can override it). Reject API redirects with `ApiRedirectError`, retaining status and response headers; requests use manual redirect handling.

- The 503 ProposalUnavailable body includes proposal_not_recorded and workspace_lock_timeout. isRetryableProposalError(status, error) narrows the known retryable body; result.response.headers retains Retry-After.
- Regenerate from core main `40a2c3f1563aaa489d5658ef6058ffb6a613709c` with the existing pinned generator and settings.
- Include core contract changes: bounded Actions and Launch projections/continuations, rule summaries, workspace creative and account inventory reads, frozen target evidence, and delivery incident attention/held states. The unused DeploymentPlan schema is removed upstream; creative MCP metadata schemas reflect the template-only connector contract.

### Breaking changes

- `DeploymentPlan` and `zDeploymentPlan` are removed. Migration: use `DeploymentPlanRead` and `zDeploymentPlanRead`.
- `ActionsApiProposeErrors[503]` and `LaunchPlansExecuteErrors[503]` now use `ProposalUnavailable` instead of `WorkspaceLockTimeout` (core #1063). Migration: accept the broader type and detect lock timeout by using the guarded expression `isRetryableProposalError(status, error) && error.error.code === "workspace_lock_timeout"`; a non-envelope body fails the guard without reading a missing code.
- `DeliveryStatus` adds `"held"` and `DestinationStatus` adds `"needs_attention"`, breaking exhaustive switches. Migration: add handlers for both states before the exhaustive/default rejection.
- `Destination` now requires `attention_reason`, `held_count`, and `notices`, breaking manually constructed object literals. Migration: supply all three using the generated component’s declared types when constructing `Destination`; endpoint projection types remain distinct.
- Plan `creatives` is capped at 5 by default (≤30 KB) on `plans.show` and every plan body (index, store, copy, update, validate), with `creative_count`, `next_cursor`, `truncated`, and `continuation`. Migration: request further creatives through the plan read endpoint using each returned `next_cursor` until complete; do not treat an embedded plan body as the full creative list.
- Actions batch `data.actions`, propose `proposal.actions`, and dry-run `dry_run.actions` are capped at 25 by default (≤65 KB). Migration: follow `next_cursor` with the same inputs/filters; for saved proposals continue through the batch read endpoint rather than resubmitting a write.
- Actions index and plans index pages are byte-bounded and may contain fewer than `limit`/`per_page` rows. Migration: follow the server’s `next_cursor` (raw response metadata or additional properties where omitted from generated types), not `page=n+1` after a truncated page, which can skip rows.
- Inventory metrics `metrics`, `object_metrics`, and `changes` are each capped at 25 (≤22 KB), with per-section `pagination` and a base64 `next_cursor`. Migration: follow the returned `next_cursor` as `cursor` with unchanged scope/filters until every required section is complete.

### Retry classification

- Both `workspace_lock_timeout` and `proposal_not_recorded` are retryable on propose, execute, and copy; preserve `Retry-After` when present (delta seconds or an HTTP date) when scheduling a retry. No automatic retry is added.
