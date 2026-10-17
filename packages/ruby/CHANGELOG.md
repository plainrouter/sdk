# Changelog

## 0.6.1 (Unreleased)

- Fix launcher import so it reaches the route core serves; it previously returned 404 for every caller using the default base.
- `GET /workspaces/{workspace}/admin/ad-accounts/{account_id}/inventory` and `GET /workspaces/{workspace}/admin/ad-accounts/{account_id}/inventory/metrics` now document the workspace 404, which decodes as `ApiRouteNotFound`; account-not-found 404s retain their message. Compatibility: generated `GetAccountInventory404Response` changes from a model class to an anyOf module (`.build`) that resolves to `ApiRouteNotFound` or `GetAccountInventory404ResponseAnyOf`, the former `message` model; `.new` and `.build_from_hash` are removed.
- Load Pathname for multipart uploads when Ruby runs outside Bundler.
- Reflect core #1196's stricter server behavior for the existing workspace contract: live credentials targeting foreign, inaccessible same-team, or missing workspaces, and resources inside them, now receive 404 `api_route_not_found`.
- Non-canonical workspace path IDs (including leading zeros, signs, spaces, decimals, and `true`/`false` in any case) receive the same 404, even for the caller's own workspace. Unauthenticated requests receive the same response for existing and missing workspaces.
- `workspace_id` is checked only by routes that read it; on those routes, missing, foreign, and non-canonical selectors receive the canonical-missing response, while it has no effect elsewhere. Foreign or non-canonical entries in `workspace_ids` receive the same 422 as nonexistent entries.
- Callers that branched on 401, 403, 400, or 302 for a foreign or missing workspace now receive 404 `api_route_not_found`.
- Regenerate the documented contract: `GET /agent/context` and `POST /mcp/launcher/import` now document 404 `ApiRouteNotFound`; `GET /agent/context` 403 now reads “The accessible workspace scope or operation is unauthorized, or an ambiguous workspace selection was omitted.” and 422 now reads “Invalid account ID, mismatched account binding, or ambiguous active accounts.”

## 0.6.0 (2026-10-15)

- Tighten page validation. On the actions, action-rules, tests, creatives, plans and policies lists, page is an integer from 1 to 10^16. Unset and language-null page values are omitted from requests, preserving the server default page 1. Generated APIs send integer strings such as "2" unchanged, leaving their bounds and other validation to the server, which refuses invalid values with 422 on page. The curated SDK normalizes integer strings for bounds checks and refuses booleans before sending. Values outside the bounds are refused by the SDK before sending for numeric values (and normalized curated integer strings); other invalid values are refused by the SDK before sending or by the server with 422 on page.

- Refuse unknown keys, including case variants, on closed request objects before sending; errors name the key and object. Closed objects and their allowed keys are derived from the vendored contract, including model construction, mapping conversion, and raw request bodies. Raw ApiClient requests without operation metadata resolve the same schema from their HTTP method and path.
- Expose the regenerated Launch policy index, create and retire operations and draft-batch file import through the curated client, preserving its shared header, Accept and redirect policy.
- Tighten validation of the existing contract: integer inputs refuse JSON booleans instead of treating them as 1 or 0. The curated client rejects booleans before sending with an error naming the integer field; integer selectors are generated from the contract, and integers and numeric strings remain accepted.
- Tighten existing Action params validation: all 14 variants accept only their documented keys; extra keys, including case variants, fail with `action_params_invalid`.
- Document `launch_video_upload_unavailable` for Launch plans that require a new Meta video upload, at validation and execution.
- Include newly documented integer-boolean 422 responses, the plan validate 422 code, creative-list 404 and 403 responses, and corrected descriptions.

- Correct `actions.api.index`, `actions.api.policy`, `actions.api.show`, `actions.api.batch`, and `actions.api.decision-receipt` errors: 401 is `AgentCredentialError` or `ErrorMessage`, and 403 is `AgentCredentialError`; list, policy, show, and batch 404 is `ApiRouteNotFound`, while decision-receipt 404 is `ActionReceiptUnavailable` or `ApiRouteNotFound`. Remove `enabled` from action-rule create requests and `platform_ad_account_id` from update requests; both fields are prohibited by the contract.
- Curate the previously generated-only `actions.api.dry-run`, `actions.api.index`, `actions.api.policy`, `actions.api.decision-receipt`, `actions.api.show`, `actions.api.batch`, `actions.rules.index`, `actions.rules.store`, `actions.rules.show`, `actions.rules.update`, `actions.tests.api.index`, `actions.tests.api.store`, `actions.tests.api.show`, `agent.context`, `getCookieDeclaration`, `launch.creatives.index`, `storeCreative`, `storeCreativeFromUrl`, `get_account_inventory`, and `get_inventory_metrics` operations through the `action_dry_run`, `action_reads`, `action_rules`, `ad_tests`, `agent_context`, `cookie_declarations`, `creatives`, and `inventory` groups.
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
