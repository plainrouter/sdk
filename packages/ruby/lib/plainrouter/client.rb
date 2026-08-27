# frozen_string_literal: true

require "uri"

module PlainRouter
  # Compact entry point for the PlainRouter API.
  class Client
    attr_reader :events, :operations, :sandbox

    def initialize(token: nil, base_url: DEFAULT_BASE_URL, timeout: 30, user_agent: nil)
      configuration = OpenAPI::Configuration.new
      configure_base_url(configuration, base_url)
      configuration.access_token = token
      configuration.timeout = timeout
      yield configuration if block_given?

      api_client = OpenAPI::ApiClient.new(configuration)
      api_client.user_agent = user_agent || "plainrouter-ruby/#{VERSION}"

      @events = OpenAPI::EventApi.new(api_client)
      @operations = OpenAPI::OperationsApi.new(api_client)
      @sandbox = OpenAPI::SandboxApi.new(api_client)
    end

    private

    def configure_base_url(configuration, base_url)
      uri = URI.parse(base_url)
      unless uri.is_a?(URI::HTTP) && uri.host && !uri.query && !uri.fragment
        raise ArgumentError, "base_url must be an absolute HTTP(S) URL without a query or fragment"
      end

      host = uri.host
      host = "#{host}:#{uri.port}" unless uri.port == uri.default_port

      configuration.scheme = uri.scheme
      configuration.host = host
      configuration.base_path = uri.path
      configuration.ignore_operation_servers = true
    rescue URI::InvalidURIError
      raise ArgumentError, "base_url must be an absolute HTTP(S) URL without a query or fragment"
    end
  end
end
