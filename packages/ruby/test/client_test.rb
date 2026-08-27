# frozen_string_literal: true

require "minitest/autorun"
require "plainrouter"
require "faraday/adapter/test"

class PlainRouterClientTest < Minitest::Test
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
      %i[create_sandbox_key get_sandbox validate_sandbox_event validate_sandbox_event_with_key],
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
    assert_equal "Bearer tracker-secret", api_client.config.auth_settings.fetch("signalTrackerSecret").fetch(:value)
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
