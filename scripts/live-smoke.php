<?php

declare(strict_types=1);

require __DIR__.'/../packages/php/vendor/autoload.php';

use Plainrouter\Client;
use Plainrouter\OpenAPI\ApiException;
use Plainrouter\OpenAPI\Model\ErrorMessage;

$baseUrl = getenv('PLAINROUTER_BASE_URL') ?: Client::DEFAULT_BASE_URL;
$anonymous = new Client(baseUrl: $baseUrl);

try {
    $anonymous->operations->listEvents(1);
    throw new RuntimeException('Anonymous event listing must return HTTP 401.');
} catch (ApiException $error) {
    if ($error->getCode() !== 401) {
        throw $error;
    }

    $body = $error->getResponseObject();
    if (! $body instanceof ErrorMessage || $body->listInvalidProperties() !== [] || trim($body->getMessage()) === '') {
        throw new RuntimeException('Anonymous event listing returned an invalid authentication error.');
    }
}

echo "PHP SDK anonymous authorization smoke passed (401). No authenticated operations exercised.\n";
