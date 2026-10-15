# frozen_string_literal: true

require "uri"
require "date"
require "json"
require "thread"

module PlainRouter
  # Compact entry point for the Plainrouter API.
  class Client
    INTEGER_INPUT_FIELDS = JSON.parse(File.read(File.join(__dir__, "integer_input_fields.json")))
    INTEGER_INPUT_GUARD_CACHE = {}
    INTEGER_INPUT_GUARD_CACHE_LOCK = Mutex.new
    private_constant :INTEGER_INPUT_FIELDS
    private_constant :INTEGER_INPUT_GUARD_CACHE
    private_constant :INTEGER_INPUT_GUARD_CACHE_LOCK

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

    class RejectRedirects < Faraday::Middleware
      def on_complete(env)
        return unless (300...400).cover?(env.status)

        raise OpenAPI::ApiError.new(code: env.status, response_headers: env.response_headers, response_body: env.body)
      end
    end

    # Distinguish generator defaults from caller values without changing operation signatures.
    DefaultAccept = Class.new(String)
    private_constant :DefaultAccept

    class JsonApiClient < OpenAPI::ApiClient
      def initialize(configuration, accept:)
        super(configuration)
        @accept = accept
        @default_headers = Faraday::Utils::Headers.new(@default_headers)
        @default_headers["Accept"] = accept || "application/json"
      end

      def select_header_accept(accepts)
        DefaultAccept.new(super(accepts) || "application/json")
      end

      def build_request(http_method, path, request, opts = {})
        validate_integer_inputs(http_method, path, opts)

        headers = Faraday::Utils::Headers.new
        (opts[:header_params] || {}).each do |name, value|
          next if name.casecmp?("Accept") && value.is_a?(DefaultAccept)

          headers[name] = value
        end
        unless headers.key?("Accept")
          caller_accept = request.headers["Accept"]
          caller_accept = nil if caller_accept == "*/*"
          headers["Accept"] = @accept || caller_accept || @default_headers["Accept"] || "application/json"
        end
        super(http_method, path, request, opts.merge(header_params: headers))
      end

      private

      def validate_integer_inputs(http_method, path, opts)
        method_path, metadata = integer_input_operation(http_method, path)
        return unless metadata

        request_bodies = [opts[:body], opts[:form_params]].map { |body| parsed_request_body(body) }
        metadata.fetch("body").each do |segments|
          request_bodies.each do |request_body|
            field_path = boolean_integer_body_path(request_body, segments)
            refuse_boolean_integer(field_path) if field_path
          end
        end

        query_params = opts[:query_params] || {}
        metadata.fetch("query").each do |name|
          present, value = hash_value(query_params, name)
          next unless present

          field_path = boolean_integer_value_path(value, name)
          refuse_boolean_integer(field_path) if field_path
        end

        integer_path_names = metadata.fetch("path")
        return if integer_path_names.empty?

        template = method_path.split(" ", 2).last
        path_values = integer_path_values(template, path)
        integer_path_names.each do |name|
          value = path_values[name]
          next unless value == "true" || value == "false"

          refuse_boolean_integer(name)
        end
      end

      def integer_input_operation(http_method, path)
        method = http_method.to_s.upcase
        path = path.to_s
        INTEGER_INPUT_FIELDS.each do |method_path, metadata|
          entry_method, template = method_path.split(" ", 2)
          next unless entry_method == method
          next unless path_matches_template?(template, path)

          return [method_path, metadata]
        end
        [nil, nil]
      end

      def path_matches_template?(template, path)
        pattern = Regexp.escape(template).gsub(/\\\{[^}]+\\\}/, "[^/]+")
        Regexp.new("\\A#{pattern}\\z").match?(path)
      end

      def integer_path_values(template, path)
        template_parts = template.split("/")
        path_parts = path.split("/")
        return {} unless template_parts.length == path_parts.length

        template_parts.zip(path_parts).each_with_object({}) do |(template_part, path_part), values|
          match = /\A\{([^}]+)\}\z/.match(template_part)
          values[match[1]] = URI::DEFAULT_PARSER.unescape(path_part) if match
        end
      end

      def parsed_request_body(body)
        value = body.respond_to?(:to_hash) ? body.to_hash : body
        return value unless value.is_a?(String)

        JSON.parse(value)
      rescue JSON::ParserError
        nil
      end

      def boolean_integer_body_path(value, segments, field_path = "")
        return field_path if segments.empty? && boolean_value?(value)
        return nil if segments.empty?

        segment, *rest = segments
        if segment == "*"
          entries = if value.is_a?(Array)
                      value.each_with_index.map { |item, index| ["#{field_path}[#{index}]", item] }
                    elsif value.is_a?(Hash)
                      value.map do |key, item|
                        item_path = field_path.empty? ? key.to_s : "#{field_path}.#{key}"
                        [item_path, item]
                      end
                    else
                      return nil
                    end
          entries.each do |item_path, item|
            found = boolean_integer_body_path(item, rest, item_path)
            return found if found
          end
          return nil
        end

        return nil unless value.is_a?(Hash)

        present, child = hash_value(value, segment)
        return nil unless present

        child_path = field_path.empty? ? segment : "#{field_path}.#{segment}"
        boolean_integer_body_path(child, rest, child_path)
      end

      def boolean_integer_value_path(value, field_path)
        return field_path if boolean_value?(value)

        if value.is_a?(Array)
          value.each_with_index do |item, index|
            found = boolean_integer_value_path(item, "#{field_path}[#{index}]")
            return found if found
          end
        end
        nil
      end

      def hash_value(hash, name)
        return [true, hash[name]] if hash.key?(name)

        symbol = name.to_sym
        return [true, hash[symbol]] if hash.key?(symbol)

        [false, nil]
      end

      def boolean_value?(value)
        value.equal?(true) || value.equal?(false)
      end

      def refuse_boolean_integer(field_path)
        raise ArgumentError,
              "#{field_path} must not be a boolean; expected an integer or numeric string."
      end

      def normalize_generated_operation_options(method_path, options)
        return options unless options.is_a?(Hash)

        metadata = INTEGER_INPUT_FIELDS.fetch(method_path)
        option_fields = metadata.fetch("query") + metadata.fetch("body").filter_map do |segments|
          segments.first if segments.length == 1
        end
        normalized = options.dup
        option_fields.uniq.each do |name|
          present, value = hash_value(normalized, name)
          next unless present && value.is_a?(String) && /\A[+-]?\d+\z/.match?(value)

          key = normalized.key?(name) ? name : name.to_sym
          normalized[key] = value.to_i
        end
        normalized
      end

      def validate_generated_operation_inputs(method_path, argument_names, argument_values)
        metadata = INTEGER_INPUT_FIELDS.fetch(method_path)
        arguments = argument_names.zip(argument_values).to_h
        options = arguments["opts"] || arguments["options"] || {}

        metadata.fetch("body").each do |segments|
          body_candidates = arguments.filter_map do |name, value|
            next if %w[opts options].include?(name)
            next unless value.is_a?(Hash) || value.is_a?(Array) || value.respond_to?(:to_hash) || value.is_a?(String)

            parsed_request_body(value)
          end
          body_candidates.concat(
            [options, options["form_params"], options[:form_params], options["body"], options[:body], options["debug_body"], options[:debug_body]]
              .map { |body| parsed_request_body(body) }
          )
          body_candidates.each do |request_body|
            field_path = boolean_integer_body_path(request_body, segments)
            refuse_boolean_integer(field_path) if field_path
          end
        end

        metadata.fetch("query").each do |name|
          present, value = hash_value(options, name)
          unless present
            query_params = options["query_params"] || options[:query_params] || {}
            present, value = hash_value(query_params, name)
          end
          next unless present

          field_path = boolean_integer_value_path(value, name)
          refuse_boolean_integer(field_path) if field_path
        end

        metadata.fetch("path").each do |name|
          value = arguments[name]
          refuse_boolean_integer(name) if boolean_value?(value)
        end
      end
    end

    attr_reader :actions, :action_dry_run, :action_reads, :action_rules, :agent_context,
                :ad_tests, :cookie_declarations, :creatives, :events, :file_imports, :inventory,
                :launch_policies, :operations, :plans, :sandbox

    def initialize(token: nil, base_url: DEFAULT_BASE_URL, timeout: 30, user_agent: nil, accept: nil)
      configuration = OpenAPI::Configuration.new
      configure_base_url(configuration, base_url)
      configuration.access_token = token
      configuration.timeout = timeout
      yield configuration if block_given?
      configuration.configure_faraday_connection { |connection| connection.use RejectRedirects }

      api_client = JsonApiClient.new(configuration, accept: accept)
      api_client.user_agent = user_agent || "plainrouter-ruby/#{VERSION}"

      @actions = OpenAPI::ActionProposalApiApi.new(api_client)
      @action_dry_run = OpenAPI::ActionDryRunApiApi.new(api_client)
      @action_reads = OpenAPI::ActionReadApiApi.new(api_client)
      @action_rules = OpenAPI::ActionRuleApiApi.new(api_client)
      @agent_context = OpenAPI::AgentContextApi.new(api_client)
      @cookie_declarations = OpenAPI::CookieDeclarationApi.new(api_client)
      @creatives = OpenAPI::CreativeApi.new(api_client)
      @events = OpenAPI::EventApi.new(api_client)
      @events.singleton_class.prepend(EventsValidation)
      @file_imports = OpenAPI::DraftBatchFileImportApi.new(api_client)
      @inventory = OpenAPI::MetaInventoryExposureApi.new(api_client)
      @launch_policies = OpenAPI::LaunchPolicyApi.new(api_client)
      @operations = OpenAPI::OperationsApi.new(api_client)
      @sandbox = OpenAPI::SandboxApi.new(api_client)
      @plans = OpenAPI::DeploymentPlanApi.new(api_client)
      @ad_tests = OpenAPI::AdTestApiApi.new(api_client)

      [
        @actions, @action_dry_run, @action_reads, @action_rules, @ad_tests, @agent_context,
        @cookie_declarations, @creatives, @events, @file_imports, @inventory,
        @launch_policies, @operations, @plans, @sandbox
      ].each { |api_group| install_integer_input_guards(api_group) }
    end

    private

    def install_integer_input_guards(api_group)
      return if api_group.instance_variable_defined?(:@plainrouter_integer_input_guards)

      guard_module = INTEGER_INPUT_GUARD_CACHE_LOCK.synchronize do
        INTEGER_INPUT_GUARD_CACHE[api_group.class] ||= build_integer_input_guard_module(api_group.class)
      end
      api_group.singleton_class.prepend(guard_module)
      api_group.instance_variable_set(:@plainrouter_integer_input_guards, true)
    end

    def build_integer_input_guard_module(api_class)
      operation_entries = INTEGER_INPUT_FIELDS.each_with_object({}) do |(method_path, metadata), entries|
        entries[ruby_operation_name(metadata.fetch("operationId"))] = method_path
      end
      guard_module = Module.new
      api_class.instance_methods(false).grep(/_with_http_info\z/).each do |http_info_method|
        operation_method = http_info_method.to_s.delete_suffix("_with_http_info")
        method_path = operation_entries[operation_method]
        next unless method_path

        [operation_method.to_sym, http_info_method].each do |method_name|
          method = api_class.instance_method(method_name)
          signature = ruby_method_signature(method)
          argument_names = method.parameters.map { |_kind, name| name.to_s }
          argument_values = argument_names.join(", ")
          options_name = argument_names.find { |name| %w[opts options].include?(name) }
          normalize_options = options_name ? "#{options_name} = @api_client.__send__(:normalize_generated_operation_options, #{method_path.inspect}, #{options_name})" : nil
          source = <<~RUBY
            def #{method_name}(#{signature})
              #{normalize_options}
              @api_client.__send__(:validate_generated_operation_inputs, #{method_path.inspect}, #{argument_names.inspect}, [#{argument_values}])
              super
            end
          RUBY
          guard_module.module_eval(source, __FILE__, __LINE__)
        end
      end
      guard_module
    end

    def ruby_method_signature(method)
      source_path, line_number = method.source_location
      definition = File.foreach(source_path).lazy.drop(line_number - 1).first
      match = definition && /\A\s*def\s+#{Regexp.escape(method.name.to_s)}\((.*)\)\s*\z/.match(definition)
      return match[1] if match

      method.parameters.map do |kind, name|
        case kind
        when :req then name.to_s
        when :opt then "#{name} = {}"
        when :rest then "*#{name}"
        when :keyreq then "#{name}:"
        when :key then "#{name}: {}"
        when :keyrest then "**#{name}"
        when :block then "&#{name}"
        else raise ArgumentError, "Unsupported generated parameter: #{kind}"
        end
      end.join(", ")
    end

    def ruby_operation_name(operation_id)
      operation_id
        .gsub(/([A-Z]+)([A-Z][a-z])/, "\\1_\\2")
        .gsub(/([a-z0-9])([A-Z])/, "\\1_\\2")
        .gsub(/[^A-Za-z0-9]+/, "_")
        .gsub(/\A_+|_+\z/, "")
        .downcase
    end

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
