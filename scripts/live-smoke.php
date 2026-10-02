<?php

declare(strict_types=1);

require __DIR__.'/../packages/php/vendor/autoload.php';

use Plainrouter\Client;
use Plainrouter\OpenAPI\Model\GetSandbox200Response;
use Plainrouter\OpenAPI\Model\ListEvents200Response;
use Plainrouter\OpenAPI\Model\ModelInterface;
use Plainrouter\OpenAPI\Model\ValidateSandboxEvent200Response;
use Plainrouter\OpenAPI\ObjectSerializer;

$baseUrl = getenv('PLAINROUTER_BASE_URL') ?: Client::DEFAULT_BASE_URL;

/**
 * @param  class-string<ModelInterface>  $expected
 */
function assertContract(mixed $model, string $expected, string $description): void
{
    if (! $model instanceof $expected) {
        throw new RuntimeException("{$description} returned an unexpected response: ".get_debug_type($model));
    }

    $invalid = $model->listInvalidProperties();

    if ($invalid !== []) {
        throw new RuntimeException("{$description} violates the signed contract: ".implode(' ', $invalid));
    }
}

function assertDiscarded(mixed $result, string $description): void
{
    assertContract($result, ValidateSandboxEvent200Response::class, $description);

    if (! $result->getSandbox() || ! $result->getAccepted() || $result->getPersisted() || $result->getProviderDelivery()) {
        throw new RuntimeException("{$description} was not validated and discarded: ".json_encode($result));
    }
}

$anonymous = new Client(baseUrl: $baseUrl);
$sandbox = $anonymous->sandbox->getSandbox();
assertContract($sandbox, GetSandbox200Response::class, 'Sandbox discovery');

if ($sandbox->getPersistsData() || $sandbox->getProviderDelivery()) {
    throw new RuntimeException('The live sandbox no longer declares itself isolated.');
}

$body = json_decode(
    json_encode(ObjectSerializer::sanitizeForSerialization($sandbox->getTry()->getBody()), JSON_THROW_ON_ERROR),
    true,
    flags: JSON_THROW_ON_ERROR,
);
assertDiscarded($anonymous->sandbox->validateSandboxEvent($body), 'Zero-auth synthetic event');

$keyed = new Client(token: $sandbox->getSelfServeKey()->getIssuedKey()->getApiKey(), baseUrl: $baseUrl);
assertDiscarded($keyed->sandbox->validateSandboxEventWithKey($body), 'Keyed synthetic event');
echo "PHP SDK live sandbox smoke passed.\n";

$signalTrackerSecret = getenv('PLAINROUTER_SMOKE_SECRET') ?: '';

if ($signalTrackerSecret === '') {
    echo '::notice title=Authenticated live smoke skipped::PLAINROUTER_SMOKE_SECRET is not set; '
        ."only the zero-auth sandbox was exercised.\n";

    return;
}

$events = (new Client(token: $signalTrackerSecret, baseUrl: $baseUrl))->operations->listEvents(5);
assertContract($events, ListEvents200Response::class, 'Authenticated event listing');
echo "PHP SDK live authenticated read smoke passed.\n";
