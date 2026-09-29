import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from services.string_services import char_count, word_count, reverse, remove_vowels

class TestStringServices(unittest.TestCase):
    def check_cases(self, service, cases):
        for value, expected in cases:
            with self.subTest(service=service.__name__, value=value):
                response = service(value)
                status = "error" if expected is None else "success"
                self.assertEqual(response["status"], status)
                self.assertEqual(response["result"], expected)

    def test_char_count(self):
        self.check_cases(char_count, [
            ('hello', 5),
            ('hello world', 11),
            ('', 0),
            ('abc123!@#', 9),
            (None, None),
            (123, None),
            ([1, 2, 3], None),
        ])

    def test_word_count(self):
        self.check_cases(word_count, [
            ('hello world', 2),
            ('hello', 1),
            ('hello    world    python', 3),
            ('', 0),
            ('   ', 0),
            ('hello\tworld\npython', 3),
            (None, None),
            (42, None),
        ])

    def test_reverse(self):
        self.check_cases(reverse, [
            ('hello', 'olleh'),
            ('hello world', 'dlrow olleh'),
            ('a', 'a'),
            ('', ''),
            ('racecar', 'racecar'),
            ('abc123!@#', '#@!321cba'),
            (None, None),
            (12345, None),
        ])

    def test_remove_vowels(self):
        self.check_cases(remove_vowels, [
            ('hello', 'hll'),
            ('aeiou', ''),
            ('bcdfg', 'bcdfg'),
            ('HELLO', 'HLL'),
            ('HeLLo WoRLd', 'HLL WRLd'),
            ('hello world', 'hll wrld'),
            ('hello123world!@#', 'hll123wrld!@#'),
            ('', ''),
            (None, None),
            (999, None),
        ])


if __name__ == "__main__":
    unittest.main()