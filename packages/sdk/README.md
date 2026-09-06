# @plainrouter/sdk

PlainRouter is a privacy-first ad measurement and spend-governance platform for advertisers and agencies in the EU. It keeps an independent count of site arrivals and verified revenue, compares that record against what ad platforms claim, and enforces spend rules against it.

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
