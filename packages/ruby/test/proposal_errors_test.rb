# frozen_string_literal: true

require "minitest/autorun"
require "plainrouter"
require "faraday/adapter/test"

class PlainRouterProposalErrorsTest < Minitest::Test
  def test_proposal_refusals_are_typed_retryable_and_retain_retry_after
    %w[proposal_not_recorded workspace_lock_timeout].each do |code|
      %w[propose execute].each do |operation|
        envelope = { "error" => { "code" => code, "message" => "Retry the proposal." } }
        path = operation == "propose" ? "/api/v1/agent/workspaces/1/actions" : "/api/v1/workspaces/1/admin/plans/plan-test/execute"
        stubs = Faraday::Adapter::Test::Stubs.new do |stub|
          stub.post(path) { [503, { "Content-Type" => "application/json", "Retry-After" => "1" }, envelope.to_json] }
        end
        configuration = PlainRouter::OpenAPI::Configuration.new
        configuration.configure_faraday_connection { |connection| connection.adapter :test, stubs }
        api_client = PlainRouter::OpenAPI::ApiClient.new(configuration)

        error = assert_raises(PlainRouter::OpenAPI::ApiError) do
          if operation == "propose"
            PlainRouter::OpenAPI::ActionProposalApiApi.new(api_client).actions_api_propose(1, {
              actions: [], evidence: [], rationale: "Pause the ad.",
              idempotency_key: "retry-test", target_source: "human_supplied"
            })
          else
            PlainRouter::OpenAPI::DeploymentPlanApi.new(api_client).launch_plans_execute(1, "plan-test", { review_version: "review-test" })
          end
        end
        assert_equal 503, error.code
        assert_instance_of PlainRouter::OpenAPI::ProposalUnavailable, error.response_object
        assert_equal code, error.response_object.error.code
        assert_equal envelope, JSON.parse(error.response_body)
        assert error.retryable?
        assert_equal "1", error.retry_after
        stubs.verify_stubbed_calls
      end
    end
  end

  def test_unrelated_and_malformed_errors_are_not_retryable_proposal_refusals
    [
      [422, { error: { code: "proposal_not_recorded", message: "Retry." } }.to_json],
      [503, { error: { code: "unknown", message: "Failed." } }.to_json],
      [503, { error: { code: "proposal_not_recorded" } }.to_json],
      [503, "not-json"]
    ].each do |status, body|
      error = PlainRouter::OpenAPI::ApiError.new(code: status, response_body: body)
      refute error.retryable?
      assert_nil error.response_object
    end
  end
end
