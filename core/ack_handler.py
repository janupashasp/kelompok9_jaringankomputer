from typing import Any, Optional, Tuple


def validate_ack(
    message: dict[str, Any],
    pending: Optional[Tuple[str, str]]
) -> Optional[str]:

    if pending is None:
        return "unexpected_ack"

    expected_request_id, _ = pending

    if message.get("type") != "ack":
        return "invalid_ack"

    if message.get("request_id") != expected_request_id:
        return "ack_request_id_mismatch"

    if not isinstance(message.get("correct"), bool):
        return "invalid_ack"

    return None