# frozen_string_literal: true

require "minitest/autorun"
require "open3"
require "plainrouter"
require "rbconfig"
require "faraday/adapter/test"
require "socket"

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
    verify_closed_proposal_objects_refuse_unknown_keys_across_ruby_input_paths
  end

  def verify_closed_proposal_objects_refuse_unknown_keys_across_ruby_input_paths
    rule = {
      "name" => "Increase a qualified budget",
      "platform_ad_account_id" => 1,
      "definition" => {
        "target_level" => "ad_set", "action" => "increase_budget",
        "minimum_counted_arrivals" => 1, "cost_comparison" => "at_least",
        "cost_ratio" => 1, "budget_change_percent" => 1
      }
    }
    rule_requests = []
    rule_stubs = Faraday::Adapter::Test::Stubs.new do |stub|
      stub.post(%r{/agent/workspaces/7/action-rules\z}) do |environment|
        rule_requests << JSON.parse(environment.body)
        [204, {}, ""]
      end
    end
    api_client = stubbed_client(rule_stubs).actions.api_client
    options = { body: rule, header_params: { "Content-Type" => "application/json" }, query_params: {}, form_params: {} }
    api_client.call_api("POST", "/api/v1/agent/workspaces/7/action-rules", options)
    assert_equal [rule], rule_requests
    bad_rule = rule.merge("definition" => rule["definition"].merge("review_extra" => 1))
    rule_error = assert_raises(ArgumentError) do
      api_client.call_api("POST", "/api/v1/agent/workspaces/7/action-rules", options.merge(body: bad_rule))
    end
    assert_includes rule_error.message, "review_extra"
    assert_includes rule_error.message, "definition"
    assert_equal [rule], rule_requests
    rule_stubs.verify_stubbed_calls

    openapi = PlainRouter::OpenAPI
    params_cases = [
      [
        openapi::ActionProposalInputActionsInnerAnyOfParams,
        { "new_daily_budget_minor" => 12_000 },
        "New_daily_budget_minor",
        "increase_budget"
      ],
      [
        openapi::ActionProposalInputActionsInnerAnyOf12Params,
        { "status" => "active" },
        "Status",
        "set_status"
      ],
      [
        openapi::ActionProposalInputActionsInnerAnyOf13Params,
        { "asset_id" => "image:asset-123", "status" => "paused" },
        "Asset_id",
        "duplicate_ad_with_creative"
      ]
    ]

    params_cases.each do |model, documented_attributes, case_variant, action_type|
      expected_attributes = documented_attributes.transform_keys(&:to_sym)
      assert_equal expected_attributes, model.new(documented_attributes).to_hash
      assert_equal expected_attributes, model.build_from_hash(documented_attributes).to_hash

      documented_body = proposal_body_with_action(action_type, documented_attributes)
      typed_body = symbolize_request_body(documented_body)
      [openapi::ActionProposalInput.new(typed_body), openapi::ActionProposalInput.build_from_hash(typed_body)].each do |proposal|
        assert_equal documented_attributes, JSON.parse(proposal.to_hash.to_json).dig("actions", 0, "params")
      end

      sent_body = nil
      stubs = Faraday::Adapter::Test::Stubs.new do |stub|
        stub.post("/api/v1/agent/workspaces/1/actions") do |environment|
          sent_body = JSON.parse(environment.body)
          [200, { "Content-Type" => "application/json" }, "{}"]
        end
      end
      stubbed_client(stubs).actions.actions_api_propose(1, documented_body, { debug_return_type: "Object" })
      assert_equal documented_attributes, sent_body.dig("actions", 0, "params")
      stubs.verify_stubbed_calls

      ["sdk_unknown_key", case_variant].each do |unknown_key|
        [
          -> { model.new(documented_attributes.merge(unknown_key => true)) },
          -> { model.build_from_hash(documented_attributes.merge(unknown_key => true)) }
        ].each do |build_model|
          error = assert_raises(ArgumentError, &build_model)
          assert_includes error.message, unknown_key
          assert_includes error.message, model.name.split("::").last
        end

        request_body = proposal_body_with_action(action_type, documented_attributes.merge(unknown_key => true))
        error = assert_raises(ArgumentError) do
          openapi::ActionProposalInput.new(request_body)
        end
        assert_includes error.message, unknown_key
        assert_includes error.message, "ActionProposalInput"

        error = assert_raises(ArgumentError) do
          stubbed_client(Faraday::Adapter::Test::Stubs.new).actions.actions_api_propose(
            1,
            request_body,
            { debug_return_type: "Object" }
          )
        end
        assert_includes error.message, unknown_key
        assert_includes error.message, "ActionProposalInput"

        error = assert_raises(ArgumentError) do
          openapi::ActionProposalInput.build_from_hash(request_body)
        end
        assert_includes error.message, unknown_key
        assert_includes error.message, "ActionProposalInput"

        error = assert_raises(ArgumentError) do
          stubbed_client(Faraday::Adapter::Test::Stubs.new).actions.api_client.call_api(
            :POST,
            "/api/v1/agent/workspaces/1/actions",
            { header_params: {}, body: request_body }
          )
        end
        assert_includes error.message, unknown_key
        assert_includes error.message, "ActionProposalInput"
      end
    end

    evidence_model = openapi::ActionProposalInputEvidenceInner
    documented_evidence = { "source_tool" => "get_account_state", "fields_used" => ["spend"] }
    expected_evidence = documented_evidence.transform_keys(&:to_sym)
    assert_equal expected_evidence, evidence_model.new(documented_evidence).to_hash
    assert_equal expected_evidence, evidence_model.build_from_hash(documented_evidence).to_hash

    ["sdk_unknown_key", "Fields_used"].each do |unknown_key|
      [
        -> { evidence_model.new(documented_evidence.merge(unknown_key => true)) },
        -> { evidence_model.build_from_hash(documented_evidence.merge(unknown_key => true)) }
      ].each do |build_model|
        error = assert_raises(ArgumentError, &build_model)
        assert_includes error.message, unknown_key
        assert_includes error.message, evidence_model.name.split("::").last
      end

      request_body = proposal_body_with_action("increase_budget", { "new_daily_budget_minor" => 12_000 })
      request_body["evidence"] = [documented_evidence.merge(unknown_key => true)]
      error = assert_raises(ArgumentError) do
        stubbed_client(Faraday::Adapter::Test::Stubs.new).actions.api_client.call_api(
          :POST,
          "/api/v1/agent/workspaces/1/actions",
          { header_params: {}, body: request_body }
        )
      end
      assert_includes error.message, unknown_key
      assert_includes error.message, "ActionProposalInput.evidence[0]"
    end

    sent_body = nil
    stubs = Faraday::Adapter::Test::Stubs.new do |stub|
      stub.post("/api/v1/agent/workspaces/1/actions") do |environment|
        sent_body = JSON.parse(environment.body)
        [200, { "Content-Type" => "application/json" }, "{}"]
      end
    end
    open_body = {
      "actions" => [],
      "rationale" => "Keep this additional open request field.",
      "idempotency_key" => "open-object-control",
      "evidence" => [{ "source_tool" => "get_account_state", "fields_used" => ["spend"] }],
      "target_source" => "test",
      "sdk_open_key" => true
    }
    stubbed_client(stubs).actions.actions_api_propose(1, open_body, { debug_return_type: "Object" })

    assert_equal true, sent_body.fetch("sdk_open_key")
    stubs.verify_stubbed_calls
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

  def test_standalone_ruby_multipart_upload_sends_request_and_surfaces_error_without_bundler
    response_body = { "error" => { "code" => "api_route_not_found", "message" => "loopback" } }.to_json
    server = TCPServer.new("127.0.0.1", 0)
    port = server.addr[1]
    capture = Thread.new do
      socket = server.accept
      raw_headers = +""
      raw_headers << socket.readpartial(4096) until raw_headers.include?("\r\n\r\n")
      request_headers, body = raw_headers.split("\r\n\r\n", 2)
      body ||= +""
      content_length = request_headers[/\r\nContent-Length:\s*(\d+)/i, 1].to_i
      body << socket.readpartial(content_length - body.bytesize) while body.bytesize < content_length
      socket.write("HTTP/1.1 404 Not Found\r\nContent-Type: application/json\r\nContent-Length: #{response_body.bytesize}\r\nConnection: close\r\n\r\n#{response_body}")
      [request_headers, body]
    rescue IOError, Errno::EBADF
      nil
    ensure
      socket&.close
    end

    script = <<~'RUBY'
      require "json"
      require "tempfile"
      raise "Bundler was loaded" if defined?(Bundler) || $LOADED_FEATURES.any? { |path| path.include?("bundler") }
      require "plainrouter"
      client = PlainRouter::Client.new(base_url: "http://127.0.0.1:#{ARGV.fetch(0)}/api/v1")
      Tempfile.create("plainrouter-multipart") do |file|
        file.write("id,name\\n1,loopback\\n")
        file.flush
        begin
          client.file_imports.launcher_file_import(
            file, "123", "456", PlainRouter::OpenAPI::DraftBatchMode::DUPLICATE_ADSET
          )
          raise "expected the loopback 404 to surface as ApiError"
        rescue PlainRouter::OpenAPI::ApiError => error
          puts JSON.generate(status: error.code, body: error.response_body)
        end
      end
    RUBY
    package_dir = File.expand_path("..", __dir__)
    env = {
      "PATH" => ENV.fetch("PATH"),
      "HOME" => ENV.fetch("HOME"),
      "TMPDIR" => ENV["TMPDIR"],
      "GEM_HOME" => ENV["GEM_HOME"] || Gem.dir,
      "GEM_PATH" => Gem.path.join(File::PATH_SEPARATOR)
    }.compact
    stdout, stderr, status = Open3.capture3(
      env, RbConfig.ruby, "-Ilib", "-e", script, port.to_s,
      chdir: package_dir, unsetenv_others: true
    )
    server.close
    captured = capture.value

    assert status.success?, "standalone ruby failed: #{stderr}#{stdout}"
    assert_equal({ "status" => 404, "body" => response_body }, JSON.parse(stdout))
    refute_nil captured, "loopback server did not receive the multipart request"
    request_headers, request_body = captured
    assert_match(/\APOST \/api\/v1\/mcp\/launcher\/import HTTP\/1\.1\z/, request_headers.lines.first.chomp)
    assert_match(/Content-Type: multipart\/form-data; boundary=/i, request_headers)
    assert_includes request_body, 'name="file"; filename="plainrouter-multipart'
    assert_includes request_body, "loopback"
  ensure
    server&.close unless server&.closed?
    capture&.kill if capture&.alive?
  end

  def test_new_workspace_404_operations_keep_the_existing_api_error_in_all_call_modes
    cases = [
      [:get, "/api/v1/agent/context", ->(client, _file) { client.agent_context.agent_context }],
      [:get, "/api/v1/agent/context", ->(client, _file) { client.agent_context.agent_context_with_http_info }],
      [:post, "/api/v1/mcp/launcher/import", ->(client, file) { client.file_imports.launcher_file_import(file, "123", "456", PlainRouter::OpenAPI::DraftBatchMode::DUPLICATE_ADSET) }],
      [:post, "/api/v1/mcp/launcher/import", ->(client, file) { client.file_imports.launcher_file_import_with_http_info(file, "123", "456", PlainRouter::OpenAPI::DraftBatchMode::DUPLICATE_ADSET) }]
    ]

    cases.each do |method, path, call|
      request_method, request_path = method == :get ? ["GET", "/agent/context"] : ["POST", "/mcp/launcher/import"]
      response_body = {
        "error" => {
          "code" => "api_route_not_found",
          "message" => "Workspace is nonexistent, inaccessible or noncanonical.",
          "resolution" => "Check the workspace selector and retry."
        },
        "request" => { "method" => request_method, "path" => request_path },
        "resources" => { "documentation" => "https://plainrouter.com/docs", "openapi" => "https://plainrouter.com/openapi.json" }
      }.to_json
      stubs = Faraday::Adapter::Test::Stubs.new do |stub|
        response = [404, { "Content-Type" => "application/json" }, response_body]
        if method == :get
          stub.get(path) { response }
        else
          stub.post(path) { response }
        end
      end
      client = PlainRouter::Client.new(base_url: "http://127.0.0.1:4567/api/v1") do |configuration|
        configuration.configure_faraday_connection { |connection| connection.adapter :test, stubs }
      end
      File.open(__FILE__, "rb") do |file|
        error = assert_raises(PlainRouter::OpenAPI::ApiError) { call.call(client, file) }
        assert_equal 404, error.code
        assert_equal response_body, error.response_body
      end
      stubs.verify_stubbed_calls
    end
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
    [["Accept", nil], ["ACCEPT", nil], ["accept", nil], ["Accept", "2"]].each do |name, generated_page|
      path = generated_page ? "/api/v1/workspaces/1/admin/creatives?page=2" : "/api/v1/dashboard/events"
      stubs = Faraday::Adapter::Test::Stubs.new do |stub|
        stub.get(path) do |env|
          assert_equal "page=2", env.url.query if generated_page
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
      assert_raises(PlainRouter::OpenAPI::ApiError) do
        headers = { name => "text/html", "authorization" => "caller-token" }
        if generated_page
          generated = PlainRouter::OpenAPI::CreativeApi.new(client.creatives.api_client)
          generated.launch_creatives_index(1, page: generated_page, header_params: headers)
        else
          client.operations.list_events(header_params: headers)
        end
      end
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

  def proposal_body_with_action(action_type, params)
    {
      "actions" => [{
        "type" => action_type,
        "target_entity" => { "type" => "campaign", "id" => "123" },
        "params" => params,
        "rationale" => "Test the closed request boundary.",
        "idempotency_key" => "closed-action-test"
      }],
      "rationale" => "Test the closed request boundary.",
      "idempotency_key" => "closed-key-test",
      "evidence" => [{ "source_tool" => "get_account_state", "fields_used" => ["spend"] }],
      "target_source" => "human_supplied"
    }
  end

  def symbolize_request_body(value)
    case value
    when Hash
      value.to_h { |key, child| [key.to_sym, symbolize_request_body(child)] }
    when Array
      value.map { |child| symbolize_request_body(child) }
    else
      value
    end
  end

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
