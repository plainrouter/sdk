# @plainrouter/sdk

Official TypeScript client and Zod schemas for [Plainrouter](https://plainrouter.com), generated from Plainrouter's signed OpenAPI contract. Plainrouter provides Meta Conversions API (CAPI) and Meta Ads MCP tooling with first-party conversion diagnostics and governed ad actions (`Ask`, `Custom`, or `Full` modes).

Official project: [plainrouter.com](https://plainrouter.com) ·
[documentation](https://plainrouter.com/docs) ·
[TypeScript SDK guide](https://plainrouter.com/docs/sdk/typescript) ·
[MCP overview](https://plainrouter.com/docs/mcp/overview) ·
[source](https://github.com/plainrouter/sdk/tree/main/packages/sdk)

Report SDK issues in the [Plainrouter SDK issue tracker](https://github.com/plainrouter/sdk/issues).

This package is in `0.x` development. Its interface is unstable and carries no
support promise yet.

Install the package:

```sh
npm install @plainrouter/sdk
```

Configure authentication by injecting a `signalTrackerSecret` bearer token with
the exported client configuration helper. No credential is embedded in the
package.

Copy a failed plan to a fresh draft with a plan-writer bearer token:

```typescript
import { configurePlainrouter, launchPlansCopy } from '@plainrouter/sdk';

configurePlainrouter({ signalTrackerSecret: process.env.PLAINROUTER_TOKEN! });
const result = await launchPlansCopy({
  path: { workspace: 1, deployment_plan: 'failed-plan-id' },
});
```

`configurePlainrouter()` defaults to `Accept: application/json`. Override it with `headers: { Accept: "..." }` in configuration or per call. API redirects use manual handling and throw `ApiRedirectError`, carrying `status`, `headers`, and `response`, regardless of `throwOnError` or result style. Browsers can hide cross-origin redirect status and Location (opaque redirects); these fail without returning data. These defaults apply to the configured SDK client. Independently constructed generated clients require their own transport policy.

The six paginated list operations accept `page` values from 1 through `10^16`. JavaScript cannot exactly represent every integer above Number.MAX_SAFE_INTEGER, and the validation schemas refuse values above it. The request functions send any number they are given; the server validates the page bounds.
