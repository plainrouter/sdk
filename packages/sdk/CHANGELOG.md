# Changelog

## 0.10.1 (Unreleased)

- Fix launcher import so it reaches the route core serves; it previously returned 404 for every caller using the default base.
- Reflect core #1196's stricter server behavior for the existing workspace contract: live credentials targeting foreign, inaccessible same-team, or missing workspaces, and resources inside them, now receive 404 `api_route_not_found`.
- Non-canonical workspace path IDs (including leading zeros, signs, spaces, decimals, and `true`/`false` in any case) receive the same 404, even for the caller's own workspace. Unauthenticated requests receive the same response for existing and missing workspaces.
- `workspace_id` is checked only by routes that read it; on those routes, missing, foreign, and non-canonical selectors receive the canonical-missing response, while it has no effect elsewhere. Foreign or non-canonical entries in `workspace_ids` receive the same 422 as nonexistent entries.
- Callers that branched on 401, 403, 400, or 302 for a foreign or missing workspace now receive 404 `api_route_not_found`.
- Regenerate the documented contract: `GET /agent/context` and `POST /mcp/launcher/import` now document 404 `ApiRouteNotFound`; `GET /agent/context` 403 now reads “The accessible workspace scope or operation is unauthorized, or an ambiguous workspace selection was omitted.” and 422 now reads “Invalid account ID, mismatched account binding, or ambiguous active accounts.”

## 0.10.0 (2026-10-15)

- Tighten page validation. On the actions, action-rules, tests, creatives, plans and policies lists, page is an integer from 1 to 10^16. Unset and language-null page values are omitted from requests, preserving the server default page 1. Integer strings such as "2" are accepted at runtime. Values outside the bounds and other invalid values are refused by the server with 422 on page; the curated SDK refuses booleans before sending. JavaScript cannot exactly represent every integer above Number.MAX_SAFE_INTEGER, and the validation schemas refuse values above it. The request functions send any number they are given; the server validates the page bounds.

- Exported request Zod parsers refuse unknown keys, including case variants, on closed contract objects instead of silently stripping them. Runtime request calls continue to send extra keys unchanged for server validation.
- Tighten validation of the existing contract: integer inputs refuse JSON booleans instead of treating them as 1 or 0. The curated client rejects booleans before sending with an error naming the integer field; integer selectors are generated from the contract, and integers and numeric strings remain accepted.
- Tighten existing Action params validation: all 14 variants accept only their documented keys; extra keys, including case variants, fail with `action_params_invalid`.
- Document `launch_video_upload_unavailable` for Launch plans that require a new Meta video upload, at validation and execution.
- Include newly documented integer-boolean 422 responses, the plan validate 422 code, creative-list 404 and 403 responses, and corrected descriptions.

- Correct `actions.api.index`, `actions.api.policy`, `actions.api.show`, `actions.api.batch`, and `actions.api.decision-receipt` errors: 401 is `AgentCredentialError` or `ErrorMessage`, and 403 is `AgentCredentialError`; list, policy, show, and batch 404 is `ApiRouteNotFound`, while decision-receipt 404 is `ActionReceiptUnavailable` or `ApiRouteNotFound`. Remove `enabled` from action-rule create requests and `platform_ad_account_id` from update requests; both fields are prohibited by the contract.
- Normalize header names case-insensitively for plain objects, `Headers` instances, tuple arrays and array-value request options before generated merging, on every operation including those that send a body. Caller headers replace defaults, except that on a client configured with a token the SDK's token is sent as Authorization on operations that authenticate unless a per-call `auth` option overrides it. Accept and Authorization each send at most one header line, and tuple indexes never become header names.

- Add `GET /agent/context` and action-rule `POST` collection, item `GET`, and item `PATCH` operations.
- Correct Destination `config`, `attention_reason`, `held_count` and `notices` types; expose plans-list `last_page`, `next_cursor`, `truncated`, `next_page_arguments` and `continuation`; clarify that `account_id` is the internal platform-account ID; correct action-rule list authentication and account/workspace selectors; fix the empty-array branches of action-rule write unions so Python generation succeeds with `--fail-on-warning`.

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
