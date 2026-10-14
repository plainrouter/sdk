# Changelog

## 0.10.0 (unreleased)

- Add `GET /agent/context` and action-rule `POST` collection, item `GET`, and item `PATCH` operations.
- Correct Destination `config`, `attention_reason`, `held_count` and `notices` types; expose plans-list `last_page`, `next_cursor`, `truncated`, `next_page_arguments` and `continuation`; clarify that `account_id` is the internal platform-account ID; correct action-rule list authentication and account/workspace selectors; fix the empty-array branches of action-rule write unions so Python generation succeeds with `--fail-on-warning`.
- Generate the SDK operation exports before standalone CLI workspace typecheck, tests and build; build the SDK dependency before the CLI build.

- Redirect errors include HTTP status and the Location header when present.

- Use the SDK JSON Accept default and reject API redirects instead of reporting a redirected HTML page as successful data.

- Align the CLI and its SDK dependency with TypeScript SDK 0.10.0; existing CLI command behavior is unchanged.
