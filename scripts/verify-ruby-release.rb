#!/usr/bin/env ruby
# frozen_string_literal: true

require "json"

root = File.expand_path("..", __dir__)
require File.join(root, "packages/ruby/lib/plainrouter/version")

tag = ENV.fetch("GITHUB_REF_NAME")
expected_tag = "ruby-v#{PlainRouter::VERSION}"
abort "release tag #{tag.inspect} does not match #{expected_tag.inspect}" unless tag == expected_tag

contract = JSON.parse(File.read(File.join(root, "spec/openapi.json")))
abort "OpenAPI contract is not signed" unless contract["x-signed"] == true
unless contract.dig("info", "version") == PlainRouter::CONTRACT_VERSION
  abort "Ruby contract version does not match spec/openapi.json"
end

puts "Verified #{tag} for signed OpenAPI #{PlainRouter::CONTRACT_VERSION}."
