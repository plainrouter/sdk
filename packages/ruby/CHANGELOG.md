# Changelog

## 0.6.0 (unreleased)

- Add `GET /agent/context` and action-rule `POST` collection, item `GET`, and item `PATCH` operations.
- Correct Destination `config`, `attention_reason`, `held_count` and `notices` types; expose plans-list `last_page`, `next_cursor`, `truncated`, `next_page_arguments` and `continuation`; clarify that `account_id` is the internal platform-account ID; correct action-rule list authentication and account/workspace selectors; fix the empty-array branches of action-rule write unions so Python generation succeeds with `--fail-on-warning`.

- The `api_client.default_headers` Accept override takes effect from this release; it had no effect before. Per-call `header_params` overrides remain supported in any header-name case, including Accept; they take precedence over `accept:`. Caller Faraday Accept is retained when `accept:` is omitted; an exact wildcard counts as unset.
- The hand-written `Client::JsonApiClient` and `Client::RejectRedirects` transport classes apply this policy to the curated groups.

- Default the hand-written client to `Accept: application/json`; override with `accept:`. API 3xx responses raise `OpenAPI::ApiError` with status and Location without following redirects. Actions propose is available through the hand-written client's `actions` service group.

- ApiError#response_object decodes the known 503 ProposalUnavailable body, #retryable? identifies it, and #retry_after exposes Retry-After without changing the exception class.
- Regenerate from core main `40a2c3f1563aaa489d5658ef6058ffb6a613709c` with the existing pinned generator and settings.
- Include core contract changes: bounded Actions and Launch projections/continuations, rule summaries, workspace creative and account inventory reads, frozen target evidence, and delivery incident attention/held states. The unused DeploymentPlan schema is removed upstream; creative MCP metadata schemas reflect the template-only connector contract.

### Breaking changes

- `PlainRouter::OpenAPI::DeploymentPlan` is removed. Migration: use `PlainRouter::OpenAPI::DeploymentPlanRead`.
- `CreativeIntakeReadCreative` and `CreativeIntakeReadCreativeTags` are renamed to `LaunchCreativesIndex200ResponseCreativesDataInner` and `LaunchCreativesIndex200ResponseCreativesDataInnerTags`; `CreativeIntakeRead#creative` returns the new class. Migration: update constant references and class checks to those names under `PlainRouter::OpenAPI`.
- `Destination.new` and destination-projection models require new `attention_reason`, `held_count`, and `notices` attributes; missing required attributes can raise `ArgumentError`. Migration: provide these attributes using each generated model’s declared types rather than constructing an incomplete destination.
- Plan `creatives` is capped at 5 by default (≤30 KB) on `plans.show` and every plan body (index, store, copy, update, validate), with `creative_count`, `next_cursor`, `truncated`, and `continuation`. Migration: request further creatives through the plan read endpoint using each returned `next_cursor` until complete; do not treat an embedded plan body as the full creative list.
- Actions batch `data.actions`, propose `proposal.actions`, and dry-run `dry_run.actions` are capped at 25 by default (≤65 KB). Migration: follow `next_cursor` with the same inputs/filters; for saved proposals continue through the batch read endpoint rather than resubmitting a write.
- Actions index and plans index pages are byte-bounded and may contain fewer than `limit`/`per_page` rows. Migration: follow the server’s `next_cursor` (raw response metadata or additional properties where omitted from generated types), not `page=n+1` after a truncated page, which can skip rows.
- Inventory metrics `metrics`, `object_metrics`, and `changes` are each capped at 25 (≤22 KB), with per-section `pagination` and a base64 `next_cursor`. Migration: follow the returned `next_cursor` as `cursor` with unchanged scope/filters until every required section is complete.

### Retry classification

- Both `workspace_lock_timeout` and `proposal_not_recorded` are retryable on propose, execute, and copy; preserve `Retry-After` when present (delta seconds or an HTTP date) when scheduling a retry. No automatic retry is added.
