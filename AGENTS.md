# PlainRouter SDK agent guide

This public repository contains the generated TypeScript, Python, and Ruby SDKs, the CLI, and agent integration metadata for PlainRouter.

## Source of truth

- `spec/openapi.json` is the checked-in copy of PlainRouter's signed OpenAPI contract.
- Keep `spec/CHECKSUM` aligned with that contract.
- Do not hand-edit generated SDK output. Change or refresh the contract, then use the repository generation workflow.
- Ruby files below `packages/ruby/lib/plainrouter/openapi/` and `packages/ruby/lib/plainrouter/openapi.rb` are generated. Keep the curated `PlainRouter::Client` facade outside that path.
- Never add API tokens, Signal Tracker secrets, OAuth credentials, or captured customer data.

## Verification

Use Node and npm versions from `.nvmrc` and `package.json`, then run the checks relevant to the change:

```sh
npm ci
npm run verify:spec
npm run typecheck
npm test
npm run build
```

Run `npm run smoke:production` only when a human explicitly requests a production smoke test. It is not part of ordinary local verification.

For agent integration changes, validate every JSON file, validate each `SKILL.md`, and keep the documented MCP endpoint, OAuth scope, developer index, and OpenAPI URL consistent with the public PlainRouter resources.
