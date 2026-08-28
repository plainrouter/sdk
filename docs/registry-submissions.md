# Registry submissions

Prepared 2026-08-28 for SDK-FUNNEL-1. This file prepares metadata and
submission instructions only. No registry or directory account was used, no
listing was submitted, and no credentials were added to the repository.

## Shared listing copy

Use this identity consistently across the official MCP Registry, LobeHub, and
Glama:

| Field | Prepared value |
| --- | --- |
| Display name | PlainRouter |
| MCP server name | `com.plainrouter/plainrouter` |
| Description | Independent arrival ledger and structural spend enforcement for a human-approved ad account. |
| Transport | Streamable HTTP |
| Endpoint | `https://plainrouter.com/mcp` |
| Repository | `https://github.com/plainrouter/sdk` |
| Developer documentation | `https://plainrouter.com/developers.md` |
| Authentication | OAuth 2.1; request only `mcp:use`; access is limited to the human-approved ad account. |

The endpoint is the only endpoint value to publish. Do not put an OAuth token
in the URL. Do not add a tool list to third-party directory copy; tools must be
discovered from the live MCP server rather than inferred here.

The exact README ownership marker, if the README is used as a package
verification surface, is:

```html
<!-- mcp-name: com.plainrouter/plainrouter -->
```

The current repository is an npm SDK/CLI workspace. The official Registry's
current npm ownership mechanism is an `mcpName` property in the published
package's `package.json`; this lane does not change package manifests. The
README marker above is the exact `mcp-name:` form used for package types whose
verification is performed through their rendered README.

## Official MCP Registry

### Namespace decision

The current registry authentication documentation says:

> “If you choose domain-based authentication, your server's name in `server.json` MUST be of the form `com.example.*/*`.”

`plainrouter.com` therefore maps to the authenticated reverse-DNS namespace
`com.plainrouter`, and the prepared name is `com.plainrouter/plainrouter`.
`plainrouter/plainrouter` may match the schema's broad name pattern, but it is
not the domain-authenticated form described by the current registry rules.

Sources used:

- [Current official server schema in the registry repository](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/server-json/draft/server.schema.json)
- [Official authentication and namespace rules](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/authentication.mdx)
- [Official registry requirements](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/server-json/official-registry-requirements.md)
- [Official publisher quickstart](https://modelcontextprotocol.io/registry/quickstart)
- [Official publisher CLI commands](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/cli/commands.md)

The current `main` schema was fetched from the registry repository on
2026-08-28 (registry commit
`6036804f1c62633b5e7d2927f411a6f4127f148a`). `server.json` uses the current
stable schema identifier `2025-12-11` shown by the official quickstart.

### Prepared artifact

`/server.json` is the submission file. It declares the hosted remote only; it
does not claim a local package or invent a server implementation. Its `0.3.2`
version matches the hosted server's `serverInfo.version` returned by the live
MCP `initialize` response on 2026-08-28; it is independent of SDK package
versions.

### Robin-side submission checklist

1. Install the official `mcp-publisher` binary using the [official quickstart](https://modelcontextprotocol.io/registry/quickstart), then run:

   ```bash
   mcp-publisher validate server.json
   ```

2. Authenticate the `com.plainrouter` domain namespace. Choose one of the
   official domain proof methods, DNS or HTTP. These commands require Robin's
   private signing key and account access; the key must never be committed:

   ```bash
   mcp-publisher login dns --domain "plainrouter.com" --private-key "<PRIVATE_KEY_HEX>"
   ```

   or:

   ```bash
   mcp-publisher login http --domain "plainrouter.com" --private-key "<PRIVATE_KEY_HEX>"
   ```

   For DNS, publish the proof TXT record printed by the CLI. For HTTP, host
   the proof at `https://plainrouter.com/.well-known/mcp-registry-auth` before
   retrying the login. Follow the current authentication documentation for
   key generation and propagation details.

3. After validation and domain login, Robin submits the prepared artifact:

   ```bash
   mcp-publisher publish server.json
   ```

4. Robin verifies the listing through the official API, using the exact
   published name:

   ```bash
   curl "https://registry.modelcontextprotocol.io/v0.1/servers?search=com.plainrouter/plainrouter"
   ```

`[Robin auth]` is required for domain ownership proof and publisher login.
`[Robin submit]` is required for the publish command. The lane does not run
either account action.

## LobeHub

LobeHub's current marketplace automation uses `@lobehub/market-cli`; the
official submission flow is documented in the [LobeHub repository's MCP
submission handler](https://github.com/lobehub/lobehub/blob/canary/.github/scripts/auto-handle-mcp-submission.ts).

### Robin-side submission steps

1. Ensure Node.js 22 or newer, then authenticate the LobeHub marketplace CLI
   and connect the GitHub account:

   ```bash
   npx -y @lobehub/market-cli login
   npx -y @lobehub/market-cli github connect
   ```

2. Submit the repository URL through the supported importer:

   ```bash
   npx -y @lobehub/market-cli plugin submit https://github.com/plainrouter/sdk
   ```

3. Track the asynchronous import:

   ```bash
   npx -y @lobehub/market-cli plugin list --output json
   ```

   If LobeHub presents an existing listing instead, claim it before publishing:

   ```bash
   npx -y @lobehub/market-cli plugin claim <identifier>
   npx -y @lobehub/market-cli plugin publish --dir /absolute/path/to/your-mcp
   ```

The repository is an SDK/CLI workspace, not a local MCP server implementation.
If the importer requires runnable server source, Robin should stop the import
and use LobeHub's supported remote-MCP listing path if offered; do not add a
fake start command or claim unsupported capabilities.

`[Robin auth]` is required for LobeHub login and GitHub account connection.
`[Robin submit]` is required for the import/claim/publish action. The lane
does not execute those commands.

### Prepared listing copy

- Name/title: `PlainRouter`
- MCP identity: `com.plainrouter/plainrouter`
- Description: `Independent arrival ledger and structural spend enforcement for a human-approved ad account.`
- MCP endpoint: `https://plainrouter.com/mcp`
- Transport: Streamable HTTP
- Authentication note: OAuth 2.1; request only `mcp:use`; the human-approved ad account is the access boundary.
- Repository: `https://github.com/plainrouter/sdk`
- Documentation: `https://plainrouter.com/developers.md`

## Glama

Glama's current [server directory](https://glama.ai/mcp/servers) exposes an
`Add Server` flow. Its [methodology](https://glama.ai/mcp/methodology) says
maintainers authenticate through GitHub OAuth for source listings and that
hosted connectors use remote-endpoint introspection with a sandbox credential
set. The [Glama MCP overview](https://glama.ai/) also describes indexing a
submitted repository and hosted remote connectors as separate paths.

### Preferred path: official Registry ingestion

Publish the official MCP Registry entry first, then search Glama for
`com.plainrouter/plainrouter` and the endpoint. Glama's methodology describes
ingestion of the official Registry; this avoids creating a duplicate manual
listing. Robin verifies the resulting listing and reports any metadata mismatch.

### Direct fallback, if Glama does not ingest the entry

1. Open [Glama's server directory](https://glama.ai/mcp/servers), select `Add
   Server`, and complete GitHub OAuth. `[Robin auth]`
2. If the form offers a hosted/remote connector route, enter the prepared
   endpoint and metadata below. Do not present this SDK repository as runnable
   server source; if Glama only accepts a source build, stop and use Registry
   ingestion instead.
3. If Glama requests scan credentials, provide only a non-production sandbox
   credential set through Robin's account workflow. Never provide a human's or
   customer's production advertising-account credentials. `[Robin auth]`
4. Submit the listing and verify the generated tool/schema metadata. `[Robin
   submit]`

### Prepared listing copy

- Name/title: `PlainRouter`
- MCP identity: `com.plainrouter/plainrouter`
- Description: `Independent arrival ledger and structural spend enforcement for a human-approved ad account.`
- Endpoint: `https://plainrouter.com/mcp`
- Transport: Streamable HTTP
- Authentication: OAuth 2.1; request only `mcp:use`; access is limited to the human-approved ad account.
- Repository: `https://github.com/plainrouter/sdk`
- Documentation: `https://plainrouter.com/developers.md`

The lane does not authenticate with GitHub/Glama, provide scan credentials, or
submit a directory listing.
