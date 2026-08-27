# PlainRouter Ruby SDK

The official Ruby SDK for the PlainRouter Signals Conversion API. It is generated from the repository's signed OpenAPI contract and is currently in `0.x` development.

## Install

Add the gem to your bundle:

```ruby
gem "plainrouter-sdk", "~> 0.1"
```

Then run `bundle install`. Ruby 3.2 or newer is required.

## Use

Create one client with a Signal Tracker secret and call one of the three API groups:

```ruby
require "plainrouter"

client = PlainRouter::Client.new(
  token: ENV.fetch("PLAINROUTER_TOKEN")
)

events = client.operations.list_events(per_page: 25)
event = client.events.get_event("event-id")
```

The default base URL is `https://plainrouter.com/api/v1` and the default timeout is 30 seconds. Credentials are supplied by the caller and are never embedded in the SDK.

The zero-auth sandbox uses the same client without a token:

```ruby
sandbox = PlainRouter::Client.new
example = sandbox.sandbox.get_sandbox
```

For response metadata, append `_with_http_info` to a generated operation. Models, API errors, configuration, and every generated operation are available in the deliberately separate `PlainRouter::OpenAPI` namespace.

## Development

From `packages/ruby`:

```sh
bundle install
bundle exec rake test
bundle exec rake build verify_package
```

Generated files live in `lib/plainrouter/openapi/` and `lib/plainrouter/openapi.rb`; do not edit them by hand. From the repository root, verify deterministic generation with:

```sh
scripts/check-ruby-generated.sh
```

Licensed under Apache-2.0.
