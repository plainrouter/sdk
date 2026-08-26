# Plainrouter CLI

The Plainrouter CLI is a `0.x` interface over `@plainrouter/sdk`. It adds no API
behavior: every API command delegates to one generated SDK operation.
The interface is unstable and carries no support promise yet.
This package is unrelated to the npm package `plain-router`.

Official project: [plainrouter.com](https://plainrouter.com) ·
[documentation](https://docs.plainrouter.com) ·
[source](https://github.com/wudaku/plainrouter-sdk/tree/main/packages/cli)

## Installation

Install the canonical scoped package globally:

```sh
npm i -g @plainrouter/cli
```

Or run it without a global installation:

```sh
npx @plainrouter/cli --help
```

Or install it from the official Homebrew tap:

```sh
brew install wudaku/tap/plainrouter
```

Authentication uses `PLAINROUTER_TOKEN` first, then
`$XDG_CONFIG_HOME/plainrouter/config.json` (or
`~/.config/plainrouter/config.json`). Store a token interactively with
`plainrouter auth login`; remove the stored token with `plainrouter auth logout`.
There is intentionally no `--token` option.

The API base URL defaults to `https://plainrouter.com/api/v1`. The
`PLAINROUTER_BASE_URL` environment variable or a `baseUrl` string in the config
file may override it for future regions.

Use `--json` on an API command for machine-readable response data. Otherwise,
the CLI prints a human-readable summary or table.

## Manual smoke test

This smoke is intentionally not part of CI because its final command reaches
production. Build first, then paste a tracker token without putting it in shell
history:

```sh
npm run build
read -s PLAINROUTER_TOKEN
export PLAINROUTER_TOKEN
npm run smoke:cli
unset PLAINROUTER_TOKEN
```

The script prints help for the complete command tree, then runs one real
`plainrouter events list --json` against the default production base URL.
