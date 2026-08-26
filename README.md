# Plainrouter SDK

Generated from Plainrouter's signed OpenAPI contract.

Official project: [plainrouter.com](https://plainrouter.com) ·
[documentation](https://docs.plainrouter.com) ·
[source](https://github.com/plainrouter/sdk)

This repository is in `0.x` development. Stability and support are not yet
promised.

## TypeScript SDK

Install the generated SDK:

```sh
npm install @plainrouter/sdk
```

Inject a Signal Tracker secret explicitly, then call a generated operation:

```ts
import { configurePlainrouter, listEvents } from '@plainrouter/sdk';

configurePlainrouter({
  signalTrackerSecret: process.env.PLAINROUTER_TOKEN!,
});

const response = await listEvents();
```

The default API base URL is `https://plainrouter.com/api/v1`. The SDK never
embeds credentials.

## Python SDK

Install the Python SDK:

```sh
python -m pip install plainrouter
```

```python
from plainrouter import create_client, list_events

client = create_client("your-signal-tracker-secret")
response = list_events.sync(client=client)
```

Python 3.11 or newer is required. The package version stays aligned with the
signed OpenAPI contract.

## CLI

Install the canonical scoped CLI globally:

```sh
npm i -g @plainrouter/cli
plainrouter --help
```

Or run the scoped package without installing it globally:

```sh
npx @plainrouter/cli --help
```

Provide a Signal Tracker secret without placing it in shell history:

```sh
read -s PLAINROUTER_TOKEN
export PLAINROUTER_TOKEN
plainrouter events list
unset PLAINROUTER_TOKEN
```

The same CLI is also available from the official Homebrew tap:

```sh
brew install plainrouter/tap/plainrouter
```

## Go SDK

The generated Go client is published as its own standard Go module:

```sh
go get github.com/plainrouter/sdk-go@v0.5.0
```
