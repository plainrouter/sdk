# OpenAPI spec-sync checklist

Use this checklist for every signed contract sync. The pull request must remain
unmerged until Robin countersigns it.

- [ ] Fetch `https://plainrouter.com/openapi.json` without transforming its bytes.
- [ ] Verify the fetched SHA-256 exactly matches the canonical value supplied by Robin.
- [ ] Replace `spec/openapi.json` with the verified live bytes.
- [ ] Update `spec/CHECKSUM` with the SHA-256, `info.version`, sync date, and source URL.
- [ ] Move the SDK and CLI package versions together through the `0.x` series.
- [ ] Regenerate `packages/sdk/src/generated` from `spec/openapi.json`.
- [ ] Run strict TypeScript typechecking.
- [ ] Run the SDK tests without live network calls.
- [ ] Regenerate again and confirm the committed generated output has no drift.
- [ ] Confirm the informational spec-drift check reports that live and vendored hashes match.
- [ ] Confirm all required CI checks are green.

Robin countersign: ____________________
