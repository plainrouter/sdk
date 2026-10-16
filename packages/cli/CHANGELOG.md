# Changelog

## 0.10.0 (2026-10-15)

- Through the SDK dependency, tighten page validation. On the actions, action-rules, tests, creatives, plans and policies lists, page is an integer from 1 to 10^16. Unset and language-null page values are omitted from requests, preserving the server default page 1. Integer strings such as "2" are accepted at runtime. Values outside the bounds and other invalid values are refused by the server with 422 on page; the SDK dependency refuses booleans before sending. These changes come through the SDK dependency and add no CLI commands.

- Through the SDK dependency, tighten validation of the existing contract: integer inputs refuse JSON booleans instead of treating them as 1 or 0. The curated client rejects booleans before sending with an error naming the integer field; integer selectors are generated from the contract, and integers and numeric strings remain accepted.
- Through the SDK dependency, tighten existing Action params validation: all 14 variants accept only their documented keys; extra keys, including case variants, fail with `action_params_invalid`.
- Through the SDK dependency, document `launch_video_upload_unavailable` for Launch plans that require a new Meta video upload, at validation and execution.
- Through the SDK dependency, include newly documented integer-boolean 422 responses, the plan validate 422 code, creative-list 404 and 403 responses, and corrected descriptions. These changes add no CLI commands.

- Through the SDK dependency, correct `actions.api.index`, `actions.api.policy`, `actions.api.show`, `actions.api.batch`, and `actions.api.decision-receipt` errors: 401 is `AgentCredentialError` or `ErrorMessage`, and 403 is `AgentCredentialError`; list, policy, show, and batch 404 is `ApiRouteNotFound`, while decision-receipt 404 is `ActionReceiptUnavailable` or `ApiRouteNotFound`. Remove `enabled` from action-rule create requests and `platform_ad_account_id` from update requests; both fields are prohibited by the contract. No CLI commands are added.
- The SDK dependency adds `GET /agent/context` and action-rule `POST` collection, item `GET`, and item `PATCH` operations; no CLI commands are added.
- Correct Destination `config`, `attention_reason`, `held_count` and `notices` types; expose plans-list `last_page`, `next_cursor`, `truncated`, `next_page_arguments` and `continuation`; clarify that `account_id` is the internal platform-account ID; correct action-rule list authentication and account/workspace selectors; fix the empty-array branches of action-rule write unions so Python generation succeeds with `--fail-on-warning`.
- Generate the SDK operation exports before standalone CLI workspace typecheck, tests and build; build the SDK dependency before the CLI build.

- Redirect errors include HTTP status and the Location header when present.

- Use the SDK JSON Accept default and reject API redirects instead of reporting a redirected HTML page as successful data.

- Align the CLI and its SDK dependency with TypeScript SDK 0.10.0; existing CLI command behavior is unchanged.
