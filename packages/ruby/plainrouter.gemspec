# frozen_string_literal: true

require_relative "lib/plainrouter/version"

Gem::Specification.new do |specification|
  specification.name = "plainrouter-sdk"
  specification.version = PlainRouter::VERSION
  specification.authors = ["PlainRouter"]
  specification.summary = "Official Ruby SDK for the PlainRouter Signals Conversion API"
  specification.description = "A compact Ruby client generated from PlainRouter's signed OpenAPI contract."
  specification.homepage = "https://plainrouter.com"
  specification.license = "Apache-2.0"
  specification.required_ruby_version = ">= 3.2"

  specification.metadata = {
    "bug_tracker_uri" => "https://github.com/plainrouter/sdk/issues",
    "documentation_uri" => "https://github.com/plainrouter/sdk/tree/main/packages/ruby",
    "homepage_uri" => specification.homepage,
    "rubygems_mfa_required" => "true",
    "source_code_uri" => "https://github.com/plainrouter/sdk/tree/ruby-v#{specification.version}/packages/ruby"
  }

  specification.files = Dir.chdir(__dir__) do
    Dir["LICENSE", "README.md", "lib/**/*.rb"].sort
  end
  specification.require_paths = ["lib"]

  specification.add_dependency "faraday", ">= 1.0.1", "< 3.0"
  specification.add_dependency "faraday-multipart", ">= 1.0.0", "< 2.0"
  specification.add_dependency "marcel", ">= 1.0.0", "< 2.0"
end
