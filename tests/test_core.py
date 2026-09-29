import unittest

from core.fault_injection import FaultInjector, make_incorrect_result
from core.ack_handler import validate_ack
from core.service_registry import ServiceRegistry


class TestFaultInjection(unittest.TestCase):

    def test_no_fault(self):
        injector = FaultInjector(error_rate=0)
        self.assertFalse(injector.should_inject())

    def test_always_fault(self):
        injector = FaultInjector(error_rate=1)
        self.assertTrue(injector.should_inject())

    def test_incorrect_result(self):
        result = make_incorrect_result("char_count", 10)
        self.assertNotEqual(result, 10)

    def test_matrix_fault_changes_result_without_mutating_original(self):
        for determinant in (1e16, -1e16, 0.0, 1e-16):
            with self.subTest(determinant=determinant):
                original = {
                    "determinant": determinant,
                    "inverse": None,
                }

                result = make_incorrect_result("matrix_3x3", original)

                self.assertNotEqual(result["determinant"], determinant)
                self.assertEqual(original["determinant"], determinant)


class TestAckHandler(unittest.TestCase):

    def test_valid_ack(self):
        pending = ("req-001", "reverse")

        message = {
            "type": "ack",
            "request_id": "req-001",
            "correct": True
        }

        self.assertIsNone(validate_ack(message, pending))

    def test_wrong_request_id(self):
        pending = ("req-001", "reverse")

        message = {
            "type": "ack",
            "request_id": "req-002",
            "correct": True
        }

        self.assertEqual(
            validate_ack(message, pending),
            "ack_request_id_mismatch"
        )

    def test_rejects_non_dictionary_ack(self):
        pending = ("req-001", "reverse")

        for message in (None, [], 42, "ack"):
            with self.subTest(message=message):
                self.assertEqual(
                    validate_ack(message, pending),
                    "invalid_ack",
                )

    def test_accepts_ack_reporting_incorrect_result(self):
        pending = ("req-001", "reverse")
        message = {
            "type": "ack",
            "request_id": "req-001",
            "correct": False,
        }

        self.assertIsNone(validate_ack(message, pending))


class TestServiceRegistry(unittest.TestCase):

    def test_service_active(self):
        registry = ServiceRegistry(["reverse"])
        self.assertTrue(registry.is_active("reverse"))

    def test_disable_service(self):
        registry = ServiceRegistry(["reverse"])
        registry.disable("reverse")

        self.assertFalse(registry.is_active("reverse"))

    def test_all_services_disabled(self):
        registry = ServiceRegistry([
            "reverse",
            "word_count"
        ])

        registry.disable("reverse")
        registry.disable("word_count")

        self.assertTrue(registry.all_disabled())


if __name__ == "__main__":
    unittest.main()
