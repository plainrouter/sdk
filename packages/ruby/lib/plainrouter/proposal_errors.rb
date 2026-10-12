# frozen_string_literal: true

require "json"

module PlainRouter::OpenAPI
  class ApiError
    # Generated Ruby errors retain raw bodies. Decode only the known proposal 503 envelope.
    # @return [ProposalUnavailable, nil]
    def response_object
      return nil unless code == 503

      data = JSON.parse(response_body.to_s)
      return nil unless data.is_a?(Hash) && data["error"].is_a?(Hash)
      return nil unless %w[proposal_not_recorded workspace_lock_timeout].include?(data["error"]["code"])
      return nil unless data["error"]["message"].is_a?(String)

      ProposalUnavailable.build_from_hash(data)
    rescue JSON::ParserError, ArgumentError
      nil
    end

    def retryable?
      !response_object.nil?
    end

    # Preserve delta seconds or an HTTP date verbatim; callers decide when to retry.
    def retry_after
      response_headers&.find { |name, _value| name.downcase == "retry-after" }&.last
    end
  end
end
