# Changelog

## 0.10.0 (unreleased)

- On propose/execute, the 503 ProposalUnavailable model includes proposal_not_recorded and workspace_lock_timeout. is_retryable_proposal_error(status_code, parsed) identifies the known retryable model; Response.headers retains Retry-After.
- Regenerate from core main `40a2c3f1563aaa489d5658ef6058ffb6a613709c` with the existing pinned generator and settings.
- Include core contract changes: bounded Actions and Launch projections/continuations, rule summaries, workspace creative and account inventory reads, frozen target evidence, and delivery incident attention/held states. The unused DeploymentPlan schema is removed upstream; creative MCP metadata schemas reflect the template-only connector contract.

### Breaking changes

- `models.DeploymentPlan` is removed. Migration: import and use `models.DeploymentPlanRead`.
- Propose/execute 503 lock timeouts now have `response.parsed` of type `ProposalUnavailable` and code enum `ProposalUnavailableErrorCode`, instead of `WorkspaceLockTimeout` (core #1063). Migration: detect lock timeout by checking `parsed.error.code` for `"workspace_lock_timeout"`, or use `is_retryable_proposal_error`; copy’s documented lock timeout retains `WorkspaceLockTimeout`.
- Constructors now require `attention_reason`, `held_count`, and `notices` on `Destination`, `SetDestinationTestModeResponse200Destination`, and `GetReconciliationReportResponse200ReportsItemDestination`; they require nullable `upload_deadline_at` and `freshness_basis` on `GetEventResponse200DeliveriesItem`, `GetEventResponse200EventDeliveriesItem`, `ListEventsResponse200EventsDataItemDeliveriesItem`, and `ListEventsByCursorResponse200EventsDataItemDeliveriesItem`. Migration: supply these arguments with the generated model’s declared types, passing `None` explicitly for nullable fields rather than omitting them.
- Plan `creatives` is capped at 5 by default (≤30 KB) on `plans.show` and every plan body (index, store, copy, update, validate), with `creative_count`, `next_cursor`, `truncated`, and `continuation`. Migration: request further creatives through the plan read endpoint using each returned `next_cursor` until complete; do not treat an embedded plan body as the full creative list.
- Actions batch `data.actions`, propose `proposal.actions`, and dry-run `dry_run.actions` are capped at 25 by default (≤65 KB). Migration: follow `next_cursor` with the same inputs/filters; for saved proposals continue through the batch read endpoint rather than resubmitting a write.
- Actions index and plans index pages are byte-bounded and may contain fewer than `limit`/`per_page` rows. Migration: follow the server’s `next_cursor` (raw response metadata or additional properties where omitted from generated types), not `page=n+1` after a truncated page, which can skip rows.
- Inventory metrics `metrics`, `object_metrics`, and `changes` are each capped at 25 (≤22 KB), with per-section `pagination` and a base64 `next_cursor`. Migration: follow the returned `next_cursor` as `cursor` with unchanged scope/filters until every required section is complete.

### Retry classification

- Both `workspace_lock_timeout` and `proposal_not_recorded` are retryable on propose, execute, and copy; preserve `Retry-After` when present (delta seconds or an HTTP date) when scheduling a retry. No automatic retry is added.
- Use the public `plainrouter.launch_plans_copy` facade for copy: it retains `WorkspaceLockTimeout` for lock timeout and decodes `proposal_not_recorded` as `ProposalUnavailable`. Direct generated copy parsing remains unchanged.
