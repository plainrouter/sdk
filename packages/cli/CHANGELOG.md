# Changelog

## 0.10.0 (unreleased)

- Through the SDK dependency, correct `actions.api.index`, `actions.api.policy`, `actions.api.show`, `actions.api.batch`, and `actions.api.decision-receipt` errors: 401 is `AgentCredentialError` or `ErrorMessage`, and 403 is `AgentCredentialError`; list, policy, show, and batch 404 is `ApiRouteNotFound`, while decision-receipt 404 is `ActionReceiptUnavailable` or `ApiRouteNotFound`. Remove `enabled` from action-rule create requests and `platform_ad_account_id` from update requests; both fields are prohibited by the contract. No CLI commands are added.
- The SDK dependency adds `GET /agent/context` and action-rule `POST` collection, item `GET`, and item `PATCH` operations; no CLI commands are added.
- Correct Destination `config`, `attention_reason`, `held_count` and `notices` types; expose plans-list `last_page`, `next_cursor`, `truncated`, `next_page_arguments` and `continuation`; clarify that `account_id` is the internal platform-account ID; correct action-rule list authentication and account/workspace selectors; fix the empty-array branches of action-rule write unions so Python generation succeeds with `--fail-on-warning`.
- Generate the SDK operation exports before standalone CLI workspace typecheck, tests and build; build the SDK dependency before the CLI build.

- Redirect errors include HTTP status and the Location header when present.

- Use the SDK JSON Accept default and reject API redirects instead of reporting a redirected HTML page as successful data.

- Align the CLI and its SDK dependency with TypeScript SDK 0.10.0; existing CLI command behavior is unchanged.
