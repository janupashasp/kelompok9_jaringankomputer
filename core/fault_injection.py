
import copy
import random
import threading
from typing import Any, Optional


def make_incorrect_result(service: str, correct_result: Any) -> Any:
    """Return a deliberately incorrect copy of a valid service result."""
    if service in ("char_count", "word_count"):
        return int(correct_result) + 1

    if service == "reverse":
        return str(correct_result) + "!"

    if service == "remove_vowels":
        return str(correct_result) + "a"

    if service == "matrix_3x3":
        corrupted = copy.deepcopy(correct_result)
        corrupted["determinant"] = float(corrupted["determinant"]) + 1.0
        return corrupted

    raise ValueError("cannot corrupt unknown service: %s" % service)


class FaultInjector:
    def __init__(
        self,
        error_rate: float = 0.30,
        seed: Optional[int] = None
    ) -> None:

        if not 0.0 <= error_rate <= 1.0:
            raise ValueError(
                "error_rate must be between 0.0 and 1.0"
            )

        self.error_rate = error_rate
        self._rng = random.Random(seed)
        self._lock = threading.Lock()

    def should_inject(self) -> bool:
        with self._lock:
            return self._rng.random() < self.error_rate
