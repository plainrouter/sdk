# frozen_string_literal: true

require "plainrouter"

base_url = ENV.fetch("PLAINROUTER_BASE_URL", PlainRouter::DEFAULT_BASE_URL)

def assert_contract!(model, expected, description)
  raise "#{description} returned an unexpected response: #{model.inspect}" unless model.is_a?(expected)
end

def assert_discarded!(result, description)
  assert_contract!(result, PlainRouter::OpenAPI::ValidateSandboxEvent200Response, description)
  return if result.sandbox && result.accepted && !result.persisted && !result.provider_delivery

  raise "#{description} was not validated and discarded: #{result.to_hash}"
end

anonymous = PlainRouter::Client.new(base_url: base_url)
sandbox = anonymous.sandbox.get_sandbox
assert_contract!(sandbox, PlainRouter::OpenAPI::GetSandbox200Response, "Sandbox discovery")
raise "The live sandbox no longer declares itself isolated." if sandbox.persists_data || sandbox.provider_delivery

body = PlainRouter::OpenAPI::ValidateSandboxEventRequest.build_from_hash(sandbox.try.body.to_hash)
assert_discarded!(anonymous.sandbox.validate_sandbox_event(body), "Zero-auth synthetic event")

keyed = PlainRouter::Client.new(token: sandbox.self_serve_key.issued_key.api_key, base_url: base_url)
assert_discarded!(keyed.sandbox.validate_sandbox_event_with_key(body), "Keyed synthetic event")
puts "Ruby SDK live sandbox smoke passed."

signal_tracker_secret = ENV.fetch("PLAINROUTER_SMOKE_SECRET", "")

if signal_tracker_secret.empty?
  puts "::notice title=Authenticated live smoke skipped::PLAINROUTER_SMOKE_SECRET is not set; " \
       "only the zero-auth sandbox was exercised."
else
  events = PlainRouter::Client.new(token: signal_tracker_secret, base_url: base_url).operations.list_events(per_page: 5)
  assert_contract!(events, PlainRouter::OpenAPI::ListEvents200Response, "Authenticated event listing")
  puts "Ruby SDK live authenticated read smoke passed."
end
