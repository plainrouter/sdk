# @plainrouter/sdk

PlainRouter connects first-party conversion signals and Meta account data with AI agents. Agents can inspect account context and propose changes. Supported JPEG and PNG uploads and paused ad copies require human approval. Budget and status changes are recommendations only; their execution is disabled in this release.

Generated TypeScript client and Zod schemas for PlainRouter's signed OpenAPI
contract.

Official project: [plainrouter.com](https://plainrouter.com) ·
[documentation](https://plainrouter.com/docs/sdk/typescript) ·
[source](https://github.com/plainrouter/sdk/tree/main/packages/sdk)

Report SDK issues in the [PlainRouter SDK issue tracker](https://github.com/plainrouter/sdk/issues).

This package is in `0.x` development. Its interface is unstable and carries no
support promise yet.

Configure authentication by injecting a `signalTrackerSecret` bearer token with
the exported client configuration helper. No credential is embedded in the
package.
