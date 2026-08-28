# Registry submissions

Reconciled 2026-08-28 for SDK-FUNNEL-2. PlainRouter is already published in
the official MCP Registry as `com.plainrouter/mcp`; versions `0.3.0`, `0.3.1`,
and `0.3.2` are present, and `0.3.2` is current. This file prepares future
version updates and third-party directory submissions only. No registry or
directory account was used, no listing was submitted, and no credentials were
added to the repository.

## Shared listing copy

Use this identity consistently across the official MCP Registry, LobeHub, and
Glama:

| Field | Prepared value |
| --- | --- |
| Display name | PlainRouter |
| MCP server name | `com.plainrouter/mcp` |
| Description | Inspect an approved ad account and first-party signal health, then propose policy-gated actions. |
| Transport | Streamable HTTP |
| Production endpoint | `https://plainrouter.com/mcp` |
| Sandbox endpoint | `https://plainrouter.com/mcp/sandbox` |
| Repository | `https://github.com/plainrouter/sdk` |
| Developer documentation | `https://plainrouter.com/developers.md` |
| Authentication | Production uses OAuth 2.1 with only `mcp:use` and the human-approved ad-account boundary. The sandbox accepts no credentials and returns synthetic data only. |

Publish both remotes in the official Registry. For a third-party production
listing, use `https://plainrouter.com/mcp` unless the directory explicitly
supports a separate sandbox remote. Do not put an OAuth token in either URL.
Do not add a tool list to third-party directory copy; tools must be discovered
from the live MCP server rather than inferred here.

The exact README ownership marker, if the README is used as a package
verification surface, is:

```html
<!-- mcp-name: com.plainrouter/mcp -->
```

The current repository is an npm SDK/CLI workspace. The official Registry's
current npm ownership mechanism is an `mcpName` property in the published
package's `package.json`; this lane does not change package manifests. The
README marker above is the exact `mcp-name:` form used for package types whose
verification is performed through their rendered README.

## Official MCP Registry

### Live identity and update boundary

The [live Registry query](https://registry.modelcontextprotocol.io/v0/servers?search=plainrouter)
is authoritative for the existing identity `com.plainrouter/mcp`. A remote URL
cannot be claimed by another server name, and published versions are immutable:
publishing `0.3.2` again is not an update. `/server.json` is reconciled to the
current live `0.3.2` record for source control, but Robin must set a new server
version that matches the deployed MCP server before the next publish. This
lane does not perform that version bump.

Sources used:

- [Live official Registry record](https://registry.modelcontextprotocol.io/v0/servers?search=plainrouter)
- [Official mcp-publisher 1.8.1 release](https://github.com/modelcontextprotocol/registry/releases/tag/v1.8.1)
- [Current official server schema in the registry repository](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/server-json/draft/server.schema.json)
- [Official authentication and namespace rules](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/authentication.mdx)
- [Official registry requirements](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/server-json/official-registry-requirements.md)
- [Official publisher quickstart](https://modelcontextprotocol.io/registry/quickstart)
- [Official publisher CLI commands](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/cli/commands.md)

The schema fetched on 2026-08-28 has identifier
`https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json`.
The commands below were checked against the official macOS arm64
`mcp-publisher` 1.8.1 binary. Its DNS login flags use the single-dash forms
shown here.

### Robin-side version-update checklist

1. Retain the existing P-384 `key.pem` securely for every future publish under
   this DNS identity. It is ignored by Git and must never be committed, pasted
   into an issue, or replaced unless Robin intentionally rotates the DNS proof.
   Confirm publisher version 1.8.1:

   ```bash
   chmod 600 key.pem
   mcp-publisher --version
   ```

2. Update `server.json` to the next deployed MCP server version, then validate
   the file. Reusing `0.3.2` fails because that Registry version already exists.

   ```bash
   mcp-publisher validate server.json
   ```

3. Derive the compressed P-384 public key and publish exactly one MCP proof TXT
   record at the DNS apex `plainrouter.com`:

   ```bash
   openssl ec -in key.pem -text -noout -conv_form compressed \
     | grep -A4 "pub:" | tail -n +2 | tr -d ' :\n' | xxd -r -p | base64
   ```

   The apex TXT value is:

   ```text
   v=MCPv1; k=ecdsap384; p=<PUBLIC_KEY_BASE64>
   ```

   Remove superseded MCP proof values before authenticating. There must be one
   `v=MCPv1` TXT record at the apex, not multiple records and not a record under
   `_mcp-auth` or another subdomain. `[Robin DNS auth]`

4. Extract the 48-byte P-384 private scalar and authenticate. Version 1.8.1
   defaults to Ed25519, so `-algorithm ecdsap384` is required. Omitting it
   produces `invalid seed length: expected 32 bytes, got 48`.

   ```bash
   PRIVATE_KEY_HEX="$(openssl ec -in key.pem -noout -text \
     | grep -A4 "priv:" | tail -n +2 | tr -d ' :\n')"
   mcp-publisher login dns -domain plainrouter.com \
     -private-key "$PRIVATE_KEY_HEX" -algorithm ecdsap384
   unset PRIVATE_KEY_HEX
   ```

   `[Robin auth]` is required for DNS management and publisher login.

5. Publish the new version and verify that it is the latest record:

   ```bash
   mcp-publisher publish server.json
   curl "https://registry.modelcontextprotocol.io/v0/servers?search=plainrouter"
   ```

   `[Robin submit]` is required for the publish command. The lane does not run
   any authentication, DNS, or publish action.

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
- MCP identity: `com.plainrouter/mcp`
- Description: `Inspect an approved ad account and first-party signal health, then propose policy-gated actions.`
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

Keep the official MCP Registry entry current, then search Glama for
`com.plainrouter/mcp` and the endpoint. Glama's methodology describes
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
- MCP identity: `com.plainrouter/mcp`
- Description: `Inspect an approved ad account and first-party signal health, then propose policy-gated actions.`
- Endpoint: `https://plainrouter.com/mcp`
- Transport: Streamable HTTP
- Authentication: OAuth 2.1; request only `mcp:use`; access is limited to the human-approved ad account.
- Repository: `https://github.com/plainrouter/sdk`
- Documentation: `https://plainrouter.com/developers.md`

The lane does not authenticate with GitHub/Glama, provide scan credentials, or
submit a directory listing.
