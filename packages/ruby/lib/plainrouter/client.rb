# frozen_string_literal: true

require "uri"
require "date"

module PlainRouter
  # Compact entry point for the PlainRouter API.
  class Client
    module EventsValidation
      # Keep this literal identical to app/Domains/Signals/Data/ConsentDecision.php::CAPTURED_AT_PATTERN.
      CAPTURED_AT_PATTERN = '/\A(?<datetime>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})(?:\.(?<fraction>\d{1,6}))?(?<offset>Z|[+-](?:[01]\d|2[0-3]):[0-5]\d)\z/'
      CAPTURED_AT_REGEX = Regexp.new(CAPTURED_AT_PATTERN[1...-1])

      def create_event(create_event_request, opts = {})
        data, _status_code, _headers = create_event_with_http_info(create_event_request, opts)
        data
      end

      def create_event_with_http_info(create_event_request, opts = {})
        validate_create_event_body(create_event_request)

        data, status_code, headers = super(
          create_event_request,
          opts.merge(debug_return_type: "Object")
        )

        typed_data = case status_code
                     when 200
                       OpenAPI::CreateEvent200Response.build_from_hash(data)
                     when 202
                       OpenAPI::CreateEvent202Response.build_from_hash(data)
                     else
                       data
                     end

        [typed_data, status_code, headers]
      end

      private

      def validate_create_event_body(body)
        visitor_id = event_value(body, :visitor_id)
        user_data = event_value(body, :user_data)
        return if visitor_id.nil? && user_data.nil?

        consent = event_value(body, :consent)
        captured_at = event_value(consent, :captured_at)

        if captured_at.nil?
          raise ArgumentError,
                "consent.captured_at is required when visitor_id or user_data is present (missing)."
        end

        return if valid_captured_at?(captured_at)

        raise ArgumentError,
              "consent.captured_at has invalid format; expected the strict ISO-8601 capture time grammar (invalid format)."
      end

      def event_value(value, key)
        source = value.respond_to?(:to_hash) ? value.to_hash : value
        return nil unless source.is_a?(Hash)

        source[key] || source[key.to_s]
      end

      def valid_captured_at?(value)
        return false unless value.is_a?(String)

        match = CAPTURED_AT_REGEX.match(value)
        return false unless match

        year, month, day, hour, minute, second = match[:datetime].scan(/\d+/).map(&:to_i)

        Date.valid_date?(year, month, day) && hour <= 23 && minute <= 59 && second <= 59
      end
    end

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
      @events.singleton_class.prepend(EventsValidation)
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
