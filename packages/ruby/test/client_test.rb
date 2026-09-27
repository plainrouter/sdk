# frozen_string_literal: true

require "minitest/autorun"
require "plainrouter"
require "faraday/adapter/test"

class PlainRouterClientTest < Minitest::Test
  VALID_CAPTURED_AT = "2026-08-19T12:34:56.123456+02:00"
  VALID_CAPTURED_AT_Z = "2026-08-19T10:34:56Z"

  def test_actions_models_accept_halted_and_reject_unknown_status
    batch = PlainRouter::OpenAPI::ActionBatchReadData.new(
      status: "halted",
      batch_status: "halted",
      actions: []
    )
    action = PlainRouter::OpenAPI::ActionReadItem.new(
      batch_status: "halted",
      disposition: PlainRouter::OpenAPI::ActionCurrentDisposition.new(late_restored: false)
    )

    assert_equal "halted", batch.status
    assert_equal "halted", batch.batch_status
    assert_equal "halted", action.batch_status
    assert_raises(ArgumentError) { batch.status = "unknown_status" }
  end

  def test_keeps_the_root_namespace_curated
    assert_equal(
      %i[CONTRACT_VERSION Client DEFAULT_BASE_URL OpenAPI VERSION],
      PlainRouter.constants(false).sort
    )
    assert_equal %i[events operations sandbox], PlainRouter::Client.public_instance_methods(false).sort
  end

  def test_exposes_all_signed_contract_operations_through_three_groups
    client = PlainRouter::Client.new

    assert_equal %i[create_event get_event verify_signal_ingestion], operation_names(client.events)
    assert_equal(
      %i[
        delete_user_data
        get_emq_report
        get_reconciliation_report
        list_events
        list_events_by_cursor
        replay_deliveries
        send_test_purchase
        set_destination_test_mode
      ],
      operation_names(client.operations)
    )
    assert_equal(
      %i[create_sandbox_key get_sandbox get_sandbox_key validate_sandbox_event validate_sandbox_event_with_key],
      operation_names(client.sandbox)
    )
  end

  def test_configures_bearer_auth_timeout_base_url_and_user_agent
    client = PlainRouter::Client.new(
      token: "tracker-secret",
      base_url: "http://localhost:4567/custom/v1",
      timeout: 12,
      user_agent: "test-agent/1"
    )
    api_client = client.events.api_client

    assert_same api_client, client.operations.api_client
    assert_same api_client, client.sandbox.api_client
    assert_equal "http://localhost:4567/custom/v1", api_client.config.base_url
    assert_equal 12, api_client.config.timeout
    assert_equal "Bearer tracker-secret", api_client.config.auth_settings.fetch("workspaceSecret").fetch(:value)
    assert_equal "test-agent/1", api_client.default_headers.fetch("User-Agent")
  end

  def test_uses_safe_defaults_and_allows_advanced_configuration
    yielded = false
    client = PlainRouter::Client.new do |configuration|
      yielded = true
      configuration.client_side_validation = false
    end
    configuration = client.events.api_client.config

    assert yielded
    assert_equal PlainRouter::DEFAULT_BASE_URL, configuration.base_url
    assert_equal 30, configuration.timeout
    assert_nil configuration.access_token
    refute configuration.client_side_validation
  end

  def test_rejects_ambiguous_base_urls
    ["plainrouter.com/api/v1", "https://example.com/api?token=secret", "ftp://example.com/api"].each do |url|
      assert_raises(ArgumentError) { PlainRouter::Client.new(base_url: url) }
    end
  end

  def test_sends_the_tracker_secret_as_a_bearer_token
    observed_authorization = nil
    stubs = Faraday::Adapter::Test::Stubs.new do |stub|
      stub.get("/api/v1/dashboard/events") do |environment|
        observed_authorization = environment.request_headers["Authorization"]
        [401, { "Content-Type" => "application/json" }, '{"message":"Unauthenticated."}']
      end
    end
    client = stubbed_client(stubs, token: "tracker-secret")

    error = assert_raises(PlainRouter::OpenAPI::ApiError) { client.operations.list_events }

    assert_equal 401, error.code
    assert_equal "Bearer tracker-secret", observed_authorization
    stubs.verify_stubbed_calls
  end

  def test_zero_auth_sandbox_does_not_send_an_authorization_header
    observed_authorization = :not_called
    stubs = Faraday::Adapter::Test::Stubs.new do |stub|
      stub.get("/api/v1/sandbox") do |environment|
        observed_authorization = environment.request_headers["Authorization"]
        [401, { "Content-Type" => "application/json" }, '{"message":"Unavailable."}']
      end
    end
    client = stubbed_client(stubs)

    assert_raises(PlainRouter::OpenAPI::ApiError) { client.sandbox.get_sandbox }

    assert_nil observed_authorization
    stubs.verify_stubbed_calls
  end

  def test_rejects_visitor_id_without_captured_at_before_making_a_call
    called = false
    stubs = Faraday::Adapter::Test::Stubs.new do |stub|
      stub.post("/api/v1/events") do
        called = true
        [202, { "Content-Type" => "application/json" }, '{"event_id":"unexpected","duplicate":false,"warnings":[]}']
      end
    end
    client = stubbed_client(stubs, token: "tracker-secret")

    error = assert_raises(ArgumentError) do
      client.events.create_event(
        "event_name" => "Purchase",
        "consent_basis" => "consent",
        "visitor_id" => "visitor-123"
      )
    end

    assert_match(/consent\.captured_at/i, error.message)
    assert_match(/required|missing/i, error.message)
    refute called
  end

  def test_rejects_user_data_with_a_space_separator_before_making_a_call
    called = false
    stubs = Faraday::Adapter::Test::Stubs.new do |stub|
      stub.post("/api/v1/events") do
        called = true
        [202, { "Content-Type" => "application/json" }, '{"event_id":"unexpected","duplicate":false,"warnings":[]}']
      end
    end
    client = stubbed_client(stubs, token: "tracker-secret")

    error = assert_raises(ArgumentError) do
      client.events.create_event(
        "event_name" => "Purchase",
        "consent_basis" => "consent",
        "user_data" => { "em" => "hashed-email" },
        "consent" => { "captured_at" => "2026-08-19 12:34:56+02:00" }
      )
    end

    assert_match(/consent\.captured_at/i, error.message)
    assert_match(/invalid|format|ISO/i, error.message)
    refute called
  end

  def test_sends_a_valid_captured_at_byte_identical_to_input
    observed_body = nil
    stubs = Faraday::Adapter::Test::Stubs.new do |stub|
      stub.post("/api/v1/events") do |environment|
        observed_body = environment.body
        [202, { "Content-Type" => "application/json" }, '{"event_id":"event-123","duplicate":false,"warnings":[]}']
      end
    end
    client = stubbed_client(stubs, token: "tracker-secret")

    client.events.create_event(
      "event_name" => "Purchase",
      "consent_basis" => "consent",
      "visitor_id" => "visitor-123",
      "consent" => { "captured_at" => VALID_CAPTURED_AT }
    )

    assert_includes observed_body, "\"captured_at\":\"#{VALID_CAPTURED_AT}\""
    stubs.verify_stubbed_calls
  end

  def test_sends_events_without_identity_when_captured_at_is_absent
    stubs = Faraday::Adapter::Test::Stubs.new do |stub|
      stub.post("/api/v1/events") do
        [202, { "Content-Type" => "application/json" }, '{"event_id":"event-123","duplicate":false,"warnings":[]}']
      end
    end
    client = stubbed_client(stubs, token: "tracker-secret")

    client.events.create_event("event_name" => "Purchase", "consent_basis" => "consent")

    stubs.verify_stubbed_calls
  end

  def test_treats_explicit_null_identity_fields_as_absent
    stubs = Faraday::Adapter::Test::Stubs.new do |stub|
      stub.post("/api/v1/events") do
        [202, { "Content-Type" => "application/json" }, '{"event_id":"event-123","duplicate":false,"warnings":[]}']
      end
    end
    client = stubbed_client(stubs, token: "tracker-secret")

    client.events.create_event(
      "event_name" => "Purchase",
      "consent_basis" => "consent",
      "visitor_id" => nil,
      "user_data" => nil
    )

    stubs.verify_stubbed_calls
  end

  def test_returns_a_typed_202_warning_without_throwing
    warning = {
      "code" => "consent_captured_at_invalid",
      "field" => "consent.captured_at",
      "message" => "Consent capture time must be ISO-8601."
    }
    stubs = Faraday::Adapter::Test::Stubs.new do |stub|
      stub.post("/api/v1/events") do
        [202, { "Content-Type" => "application/json" },
         { "event_id" => "event-warning", "duplicate" => false, "warnings" => [warning] }.to_json]
      end
    end
    client = stubbed_client(stubs, token: "tracker-secret")

    response = client.events.create_event("event_name" => "Purchase", "consent_basis" => "consent")

    assert_instance_of PlainRouter::OpenAPI::CreateEvent202Response, response
    assert_equal "event-warning", response.event_id
    assert_equal false, response.duplicate
    assert_equal 1, response.warnings.length
    parsed_warning = response.warnings.first
    assert_instance_of PlainRouter::OpenAPI::CreateEvent202ResponseWarningsInner, parsed_warning
    assert_equal PlainRouter::OpenAPI::IngestionWarningCode::CONSENT_CAPTURED_AT_INVALID, parsed_warning.code
    assert_equal "consent.captured_at", parsed_warning.field
    assert_equal warning["message"], parsed_warning.message
    stubs.verify_stubbed_calls
  end

  def test_returns_a_200_duplicate_without_a_warnings_field
    stubs = Faraday::Adapter::Test::Stubs.new do |stub|
      stub.post("/api/v1/events") do
        [200, { "Content-Type" => "application/json" }, '{"event_id":"event-duplicate","duplicate":true}']
      end
    end
    client = stubbed_client(stubs, token: "tracker-secret")

    response = client.events.create_event("event_name" => "Purchase", "consent_basis" => "consent")

    assert_instance_of PlainRouter::OpenAPI::CreateEvent200Response, response
    assert_equal "event-duplicate", response.event_id
    assert_equal true, response.duplicate
    refute response.respond_to?(:warnings)
    stubs.verify_stubbed_calls
  end

  def test_matches_server_captured_at_fixture_parity
    [
      [VALID_CAPTURED_AT, true],
      [VALID_CAPTURED_AT_Z, true],
      ["2026-08-19 12:34:56+02:00", false],
      ["2026-08-19T12:34:56", false],
      ["", false],
      [nil, false]
    ].each do |captured_at, valid|
      stubs = Faraday::Adapter::Test::Stubs.new do |stub|
        stub.post("/api/v1/events") do
          [202, { "Content-Type" => "application/json" }, '{"event_id":"event-123","duplicate":false,"warnings":[]}']
        end
      end
      client = stubbed_client(stubs, token: "tracker-secret")
      request = {
        "event_name" => "Purchase",
        "consent_basis" => "consent",
        "visitor_id" => "visitor-123",
        "consent" => { "captured_at" => captured_at }
      }

      if valid
        client.events.create_event(request)
        stubs.verify_stubbed_calls
      else
        error = assert_raises(ArgumentError) { client.events.create_event(request) }
        assert_match(/consent\.captured_at/i, error.message)
      end
    end
  end

  private

  def operation_names(group)
    group.public_methods(false)
      .grep_v(/_with_http_info\z/)
      .reject { |method| method == :api_client || method == :api_client= }
      .sort
  end

  def stubbed_client(stubs, token: nil)
    PlainRouter::Client.new(token: token) do |configuration|
      configuration.configure_faraday_connection do |connection|
        connection.adapter :test, stubs
      end
    end
  end
end
