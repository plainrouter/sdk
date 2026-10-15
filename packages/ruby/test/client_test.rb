# frozen_string_literal: true

require "minitest/autorun"
require "plainrouter"
require "faraday/adapter/test"

class PlainRouterClientTest < Minitest::Test
  VALID_CAPTURED_AT = "2026-08-19T12:34:56.123456+02:00"
  VALID_CAPTURED_AT_Z = "2026-08-19T10:34:56Z"

  def test_plan_copy_posts_with_auth_and_returns_a_typed_draft
    draft = {
      plan: {
        id: "draft-copy", platform_ad_account_id: 7, status: "draft", budget_amount_minor: 12345,
        validation_result: nil, validated_at: nil, approval_id: nil
      }
    }
    stubs = Faraday::Adapter::Test::Stubs.new do |stub|
      stub.post("/api/v1/workspaces/1/admin/plans/failed-plan/copy") do |environment|
        assert_equal "Bearer plan-writer-test-token", environment.request_headers["Authorization"]
        assert_equal "", environment.body
        [201, { "Content-Type" => "application/json" }, draft.to_json]
      end
    end

    response, status, = stubbed_client(stubs, token: "plan-writer-test-token")
      .plans.launch_plans_copy_with_http_info(1, "failed-plan")

    assert_equal 201, status
    assert_instance_of PlainRouter::OpenAPI::PlanCopyRead, response
    assert_equal draft, response.to_hash
    stubs.verify_stubbed_calls
  end

  def test_policy_model_accepts_current_response_and_rejects_invalid_mode
    data = {
      id: nil,
      workspace_id: 1,
      execution_mode: "full",
      outcome_check_after_hours: 24,
      anomaly_threshold_percent: "20.00"
    }
    policy = PlainRouter::OpenAPI::ActionPolicyReadData.new(data)

    assert_equal data, policy.to_hash
    assert_raises(ArgumentError) { policy.execution_mode = "unknown_mode" }
  end

  def test_actions_models_accept_halted_and_reject_unknown_status
    batch = PlainRouter::OpenAPI::ActionBatchReadData.new(
      id: "01JTESTBATCH00000000000000",
      workspace_id: 1,
      platform_ad_account_id: 1,
      status: "halted",
      batch_status: "halted",
      policy_reasons: [],
      rationale: "Pause the ad while the batch is halted.",
      idempotency_key: "test-halted-batch",
      actions: []
    )
    action = PlainRouter::OpenAPI::ActionReadItem.new(
      id: "01JTESTACTION0000000000000",
      batch_id: "01JTESTBATCH00000000000000",
      workspace_id: 1,
      type: "pause",
      target_entity_type: "ad",
      target_entity_id: "120000000000001",
      params: {},
      rationale: "Pause the ad while the batch is halted.",
      status: "blocked",
      policy_reasons: [],
      policy_result: nil,
      policy_results: [],
      batch_status: "halted",
      disposition: PlainRouter::OpenAPI::ActionCurrentDisposition.new(outcome_payload: nil, late_restored: false)
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
    assert_equal(
      %i[
        action_dry_run action_reads action_rules actions ad_tests agent_context cookie_declarations
        creatives events file_imports inventory launch_policies operations plans sandbox
      ],
      PlainRouter::Client.public_instance_methods(false).sort
    )
  end

  def test_exposes_all_signed_contract_operations_through_service_groups
    client = PlainRouter::Client.new

    generated = generated_operation_names
    curated = curated_operation_names(client)
    missing = generated - curated
    unexpected = curated - generated
    assert_equal generated, curated,
                 "Missing generated operations: #{missing.join(', ')}; curated operations absent from generated SDK: #{unexpected.join(', ')}"

    assert_equal %i[actions_api_dry_run], operation_names(client.action_dry_run)
    assert_equal(
      %i[actions_api_batch actions_api_decision_receipt actions_api_index actions_api_policy actions_api_show],
      operation_names(client.action_reads)
    )
    assert_equal(
      %i[actions_rules_index actions_rules_show actions_rules_store actions_rules_update],
      operation_names(client.action_rules)
    )
    assert_equal %i[agent_context], operation_names(client.agent_context)
    assert_equal %i[get_cookie_declaration], operation_names(client.cookie_declarations)
    assert_equal %i[launch_creatives_index launch_creatives_show launch_creatives_status store_creative store_creative_from_url], operation_names(client.creatives)
    assert_equal %i[launcher_file_import], operation_names(client.file_imports)
    assert_equal %i[launch_policies_index launch_policies_retire launch_policies_store], operation_names(client.launch_policies)
    assert_equal %i[launch_plans_copy launch_plans_execute launch_plans_index launch_plans_show launch_plans_store launch_plans_update launch_plans_validate], operation_names(client.plans)
    assert_equal %i[create_event get_event verify_signal_ingestion], operation_names(client.events)
    assert_equal %i[get_account_inventory get_inventory_metrics], operation_names(client.inventory)
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
    assert_equal %i[actions_tests_api_index actions_tests_api_show actions_tests_api_store], operation_names(client.ad_tests)
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
    assert_same api_client, client.plans.api_client
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
    [1, "1"].each do |event_time|
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
        "event_time" => event_time,
        "consent" => { "captured_at" => VALID_CAPTURED_AT }
      )

      assert_equal event_time, JSON.parse(observed_body).fetch("event_time")
      assert_includes observed_body, "\"captured_at\":\"#{VALID_CAPTURED_AT}\""
      stubs.verify_stubbed_calls
    end

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
        "event_time" => true
      )
    end

    assert_match(/event_time/, error.message)
    refute called
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

  def test_json_accept_default_override_and_redirect_errors
    ["application/json", "text/html", "*/*"].each do |accept|
      [300, 301, 302, 303, 304, 307, 308, 399].each do |status|
        stubs = Faraday::Adapter::Test::Stubs.new do |stub|
          stub.get("/api/v1/dashboard/events") do |env|
            assert_equal accept, env.request_headers["Accept"]
            [status, { "Location" => "/html" }, "<html>Redirect</html>"]
          end
        end
        client = PlainRouter::Client.new(base_url: "https://example.test/api/v1", accept: accept) do |config|
          config.configure_faraday_connection { |connection| connection.adapter :test, stubs }
        end
        error = assert_raises(PlainRouter::OpenAPI::ApiError) { client.operations.list_events }
        assert_equal status, error.code
        assert_equal "/html", error.response_headers["Location"]
        stubs.verify_stubbed_calls
      end
    end
  end

  def test_per_call_accept_overrides_are_case_insensitive_and_take_precedence
    ["Accept", "ACCEPT", "accept"].each do |name|
      stubs = Faraday::Adapter::Test::Stubs.new do |stub|
        stub.get("/api/v1/dashboard/events") do |env|
          assert_equal "text/html", env.request_headers["Accept"]
          assert_equal "Bearer ruby-test", env.request_headers["Authorization"]
          assert_equal 1, env.request_headers.keys.count { |key| key.casecmp?("Accept") }
          assert_equal 1, env.request_headers.keys.count { |key| key.casecmp?("Authorization") }
          [401, { "Content-Type" => "application/json" }, '{"message":"Unauthenticated."}']
        end
      end
      client = PlainRouter::Client.new(token: "ruby-test", accept: "text/csv") do |config|
        config.configure_faraday_connection { |connection| connection.adapter :test, stubs }
      end
      assert_raises(PlainRouter::OpenAPI::ApiError) { client.operations.list_events(header_params: { name => "text/html", "authorization" => "caller-token" }) }
      stubs.verify_stubbed_calls
    end
  end

  def test_caller_faraday_accept_is_preserved_without_constructor_override
    ["application/vnd.x+json", "*/*"].each do |accept|
      stubs = Faraday::Adapter::Test::Stubs.new do |stub|
        stub.get("/api/v1/dashboard/events") do |env|
          assert_equal accept == "*/*" ? "application/json" : accept, env.request_headers["Accept"]
          [401, { "Content-Type" => "application/json" }, '{"message":"Unauthenticated."}']
        end
      end
      client = PlainRouter::Client.new do |config|
        config.configure_faraday_connection do |connection|
          connection.headers["Accept"] = accept
          connection.adapter :test, stubs
        end
      end
      assert_raises(PlainRouter::OpenAPI::ApiError) { client.operations.list_events }
      stubs.verify_stubbed_calls
    end
  end

  def test_default_headers_accept_override_remains_supported
    stubs = Faraday::Adapter::Test::Stubs.new do |stub|
      stub.get("/api/v1/dashboard/events") do |env|
        assert_equal "text/html", env.request_headers["Accept"]
        [401, { "Content-Type" => "application/json" }, '{"message":"Unauthenticated."}']
      end
    end
    client = stubbed_client(stubs)
    client.operations.api_client.default_headers["accept"] = "text/html"
    assert_raises(PlainRouter::OpenAPI::ApiError) { client.operations.list_events }
    stubs.verify_stubbed_calls
  end

  private

  def operation_names(group)
    group.public_methods(false)
      .grep_v(/_with_http_info\z/)
      .reject { |method| method == :api_client || method == :api_client= }
      .sort
  end

  def generated_operation_names
    PlainRouter::OpenAPI.constants(false).flat_map do |constant|
      api_class = PlainRouter::OpenAPI.const_get(constant)
      next [] unless api_class.is_a?(Class)

      api_class.instance_methods(false).filter_map do |method|
        method.to_s.delete_suffix("_with_http_info").to_sym if method.to_s.end_with?("_with_http_info")
      end
    end.sort
  end

  def curated_operation_names(client)
    PlainRouter::Client.public_instance_methods(false).flat_map do |reader|
      group = client.public_send(reader)
      next [] unless group.class.instance_methods(false).any? { |method| method.to_s.end_with?("_with_http_info") }

      operation_names(group)
    end.uniq.sort
  end

  def stubbed_client(stubs, token: nil)
    PlainRouter::Client.new(token: token) do |configuration|
      configuration.configure_faraday_connection do |connection|
        connection.adapter :test, stubs
      end
    end
  end
end
