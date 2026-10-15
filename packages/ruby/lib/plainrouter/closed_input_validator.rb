# frozen_string_literal: true

require "json"
require "set"

module PlainRouter
  module OpenAPI
    module ClosedInputValidator
      MANIFEST = JSON.parse(File.read(File.join(__dir__, "closed_input_objects.json")))
      private_constant :MANIFEST

      module_function

      def validate_model!(model_class, attributes)
        return unless attributes.is_a?(Hash)

        model_type = model_class.is_a?(Module) ? model_class : model_class.class
        model_name = model_type.name.split("::").last
        pointers = MANIFEST.dig("ruby", "input_models", model_name)
        return unless pointers && !pointers.empty?

        object_pointers = pointers.select do |pointer|
          _resolved_pointer, schema = resolve_schema(pointer)
          schema_type = schema["type"]
          schema_type == "object" ||
            (schema_type.nil? && %w[properties allOf oneOf anyOf].any? { |keyword| schema.key?(keyword) })
        end
        errors = []

        object_pointers.each do |pointer|
          begin
            validate_schema(pointer, attributes, model_name)
            return
          rescue ArgumentError => error
            errors << error
          end
        end

        raise errors.first if errors.any?
      end

      def validate_request!(http_method, path, options)
        operation_name = options[:operation].to_s.split(".").last
        pointer = MANIFEST.dig("ruby", "operation_ids", operation_name)
        pointer ||= request_schema_pointer(http_method, path)
        return unless pointer

        body = options[:body]
        body = options[:form_params] if body.nil?
        body = request_body_value(body)
        return unless body.is_a?(Hash) || body.is_a?(Array)

        resolved_pointer, schema = resolve_schema(pointer)
        object_name = schema["title"] || request_object_name(operation_name, http_method, path, resolved_pointer)
        validate_schema(pointer, body, object_name)
      end

      def request_body_value(body)
        value = body.respond_to?(:to_hash) ? body.to_hash : body
        return value unless value.is_a?(String)

        JSON.parse(value)
      rescue JSON::ParserError
        nil
      end
      private_class_method :request_body_value

      def request_object_name(operation_name, http_method, path, schema_pointer)
        object_name = if operation_name.empty?
                        schema_pointer.to_s.split("/").last
                          .to_s
                          .gsub("~1", "/")
                          .gsub("~0", "~")
                      else
                        operation_name.split("_").map(&:capitalize).join
                      end
        object_name = "#{http_method.to_s.upcase} #{path}" if object_name.empty?

        "#{object_name} (#{http_method.to_s.upcase})"
      end
      private_class_method :request_object_name

      def request_schema_pointer(http_method, path)
        method = http_method.to_s.upcase
        concrete_path = path.to_s.split("?", 2).first
        concrete_path = concrete_path.sub(%r{\A/api/v1(?=/|\z)}, "")

        MANIFEST.fetch("operations").each do |method_path, schema_pointer|
          operation_method, template = method_path.split(" ", 2)
          next unless operation_method == method

          pattern = Regexp.escape(template).gsub(/\\\{[^}]+\\\}/, "[^/]+")
          return schema_pointer if Regexp.new("\\A#{pattern}\\z").match?(concrete_path)
        end

        nil
      end
      private_class_method :request_schema_pointer

      def validate_schema(pointer, value, object_path)
        value = value.to_hash if value.respond_to?(:to_hash)
        resolved_pointer, schema = resolve_schema(pointer)

        if value.is_a?(Array)
          item_pointer = schema.dig("items", "$ref")
          value.each_with_index do |item, index|
            validate_schema(item_pointer, item, "#{object_path}[#{index}]") if item_pointer
          end
        end

        if value.is_a?(Hash)
          properties = schema_properties(resolved_pointer)
          allowed_keys = properties.keys

          if schema["additionalProperties"] == false
            value.each_key do |key|
              next if allowed_keys.include?(key.to_s)

              raise ArgumentError,
                    "Unknown key #{key.to_s.inspect} in closed request object #{object_path.inspect}."
            end
          end

          properties.each do |property_name, property_schema|
            value.each do |key, child|
              next unless key.to_s == property_name

              child_pointer = property_schema["$ref"]
              validate_schema(child_pointer, child, "#{object_path}.#{property_name}") if child_pointer
            end
          end

          additional_schema = schema["additionalProperties"]
          if additional_schema.is_a?(Hash) && additional_schema["$ref"]
            value.each do |key, child|
              next if allowed_keys.include?(key.to_s)

              validate_schema(additional_schema["$ref"], child, "#{object_path}.#{key}")
            end
          end
        end

        validate_compositions(schema, value, object_path)
      end
      private_class_method :validate_schema

      def validate_compositions(schema, value, object_path)
        if schema["allOf"].is_a?(Array)
          schema["allOf"].each do |branch|
            validate_schema(branch["$ref"], value, object_path) if branch["$ref"]
          end
        end

        %w[oneOf anyOf].each do |keyword|
          branches = schema[keyword]
          next unless branches.is_a?(Array)

          selected = discriminator_matches(branches, value)
          candidates = selected.empty? ? branches : selected
          errors = []

          candidates.each do |branch|
            begin
              validate_schema(branch["$ref"], value, object_path) if branch["$ref"]
              return
            rescue ArgumentError => error
              errors << error
            end
          end

          raise errors.first if errors.any? && selected.empty?
          raise errors.first if errors.any? && selected.length == 1
        end
      end
      private_class_method :validate_compositions

      def discriminator_matches(branches, value)
        return [] unless value.is_a?(Hash)

        branch_properties = branches.map do |branch|
          branch_pointer = branch["$ref"]
          branch_pointer ? schema_properties(branch_pointer) : {}
        end
        discriminator_names = branch_properties.flat_map do |properties|
          properties.filter_map do |name, property|
            child = property["$ref"]
            next unless child

            _pointer, schema = resolve_schema(child)
            name if schema.key?("enum") || schema.key?("const")
          end
        end.uniq
        present_discriminators = discriminator_names.select do |name|
          value.keys.any? { |key| key.to_s == name }
        end
        return [] if present_discriminators.empty?

        matching = branches.each_with_index.filter_map do |branch, index|
          properties = branch_properties[index]
          matches = present_discriminators.all? do |name|
            property_pointer = properties.dig(name, "$ref")
            next false unless property_pointer

            _pointer, schema = resolve_schema(property_pointer)
            actual = value.find { |key, _child| key.to_s == name }&.last
            schema.key?("const") ? actual == schema["const"] : schema.fetch("enum", []).include?(actual)
          end
          branch if matches
        end

        matching
      end
      private_class_method :discriminator_matches

      def schema_properties(pointer, visited = Set.new)
        _resolved_pointer, schema = resolve_schema(pointer)
        properties = schema["properties"] || {}

        (schema["allOf"] || []).each do |branch|
          next unless branch["$ref"] && !visited.include?(branch["$ref"])

          visited.add(branch["$ref"])
          properties = properties.merge(schema_properties(branch["$ref"], visited))
        end

        properties
      end
      private_class_method :schema_properties

      def resolve_schema(pointer)
        seen = Set.new
        current_pointer = pointer

        loop do
          raise ArgumentError, "Cyclic schema reference at #{current_pointer}." if seen.include?(current_pointer)

          seen.add(current_pointer)
          schema = MANIFEST.fetch("schemas").fetch(current_pointer)
          return [current_pointer, schema] unless schema["$ref"]

          current_pointer = schema["$ref"]
        end
      end
      private_class_method :resolve_schema
    end
  end
end
