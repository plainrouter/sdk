# frozen_string_literal: true

require "plainrouter"

base_url = ENV.fetch("PLAINROUTER_BASE_URL", PlainRouter::DEFAULT_BASE_URL)
anonymous = PlainRouter::Client.new(base_url: base_url)

begin
  anonymous.operations.list_events(per_page: 1, debug_auth_names: [])
  raise "Anonymous event listing must return HTTP 401."
rescue PlainRouter::OpenAPI::ApiError => error
  raise unless error.code == 401

  body = JSON.parse(error.response_body)
  unless body.is_a?(Hash) && body["message"].is_a?(String) && !body["message"].strip.empty?
    raise "Anonymous event listing returned an invalid authentication error."
  end
end

puts "Ruby SDK anonymous authorization smoke passed (401). No authenticated operations exercised."
