# @plainrouter/sdk

Generated TypeScript client and Zod schemas for Plainrouter's signed OpenAPI
contract.

Official project: [plainrouter.com](https://plainrouter.com) ·
[documentation](https://plainrouter.com/docs/sdk/typescript) ·
[source](https://github.com/plainrouter/sdk/tree/main/packages/sdk)

Report SDK issues in the [Plainrouter SDK issue tracker](https://github.com/plainrouter/sdk/issues).

This package is in `0.x` development. Its interface is unstable and carries no
support promise yet.

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
