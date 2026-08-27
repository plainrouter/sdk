# frozen_string_literal: true

require_relative "plainrouter/version"

module PlainRouter
  DEFAULT_BASE_URL = "https://plainrouter.com/api/v1"
end

require_relative "plainrouter/openapi"
require_relative "plainrouter/client"
