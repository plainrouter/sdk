import json

import httpx

from .generated.types import Response


def is_retryable_proposal_error(status_code: int, error: object) -> bool:
    """Classify a parsed model, detailed response, HTTPX response, or raw JSON body by its envelope."""
    if status_code != 503:
        return False
    payload: object = error
    if isinstance(error, (Response, httpx.Response)):
        payload = error.content
    if isinstance(payload, (str, bytes)):
        try:
            payload = json.loads(payload)
        except (ValueError, UnicodeError):
            return False
    else:
        to_dict = getattr(payload, "to_dict", None)
        if not callable(to_dict):
            return False
        payload = to_dict()
    if not isinstance(payload, dict):
        return False
    envelope = payload.get("error")
    return (
        isinstance(envelope, dict)
        and isinstance(envelope.get("message"), str)
        and envelope.get("code") in ("workspace_lock_timeout", "proposal_not_recorded")
    )
