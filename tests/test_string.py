import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from services.string_services import (
    char_count,
    word_count,
    reverse,
    remove_vowels
)

class TestCharCount(unittest.TestCase):
    """Test cases for char_count function."""
    
    def test_char_count_simple_string(self):
        """Test char_count with simple string."""
        result = char_count("hello")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], 5)
    
    def test_char_count_with_spaces(self):
        """Test char_count includes spaces."""
        result = char_count("hello world")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], 11)  # 5 + 1 + 5
    
    def test_char_count_empty_string(self):
        """Test char_count with empty string."""
        result = char_count("")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], 0)
    
    def test_char_count_with_numbers_and_special(self):
        """Test char_count with numbers and special characters."""
        result = char_count("abc123!@#")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], 9)
    
    def test_char_count_invalid_input_none(self):
        """Test char_count with None input."""
        result = char_count(None)
        self.assertEqual(result["status"], "error")
        self.assertIsNone(result["result"])
    
    def test_char_count_invalid_input_int(self):
        """Test char_count with integer input."""
        result = char_count(123)
        self.assertEqual(result["status"], "error")
        self.assertIsNone(result["result"])
    
    def test_char_count_invalid_input_list(self):
        """Test char_count with list input."""
        result = char_count([1, 2, 3])
        self.assertEqual(result["status"], "error")
        self.assertIsNone(result["result"])


class TestWordCount(unittest.TestCase):
    """Test cases for word_count function."""
    
    def test_word_count_simple(self):
        """Test word_count with simple words."""
        result = word_count("hello world")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], 2)
    
    def test_word_count_single_word(self):
        """Test word_count with single word."""
        result = word_count("hello")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], 1)
    
    def test_word_count_multiple_spaces(self):
        """Test word_count handles multiple spaces."""
        result = word_count("hello    world    python")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], 3)
    
    def test_word_count_empty_string(self):
        """Test word_count with empty string."""
        result = word_count("")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], 0)
    
    def test_word_count_only_spaces(self):
        """Test word_count with only spaces."""
        result = word_count("   ")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], 0)
    
    def test_word_count_with_tabs_newlines(self):
        """Test word_count with tabs and newlines."""
        result = word_count("hello\tworld\npython")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], 3)
    
    def test_word_count_invalid_input_none(self):
        """Test word_count with None input."""
        result = word_count(None)
        self.assertEqual(result["status"], "error")
        self.assertIsNone(result["result"])
    
    def test_word_count_invalid_input_int(self):
        """Test word_count with integer input."""
        result = word_count(42)
        self.assertEqual(result["status"], "error")
        self.assertIsNone(result["result"])


class TestReverse(unittest.TestCase):
    """Test cases for reverse function."""
    
    def test_reverse_simple_string(self):
        """Test reverse with simple string."""
        result = reverse("hello")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], "olleh")
    
    def test_reverse_with_spaces(self):
        """Test reverse preserves spaces."""
        result = reverse("hello world")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], "dlrow olleh")
    
    def test_reverse_single_char(self):
        """Test reverse with single character."""
        result = reverse("a")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], "a")
    
    def test_reverse_empty_string(self):
        """Test reverse with empty string."""
        result = reverse("")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], "")
    
    def test_reverse_palindrome(self):
        """Test reverse with palindrome."""
        result = reverse("racecar")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], "racecar")
    
    def test_reverse_numbers_and_special(self):
        """Test reverse with numbers and special characters."""
        result = reverse("abc123!@#")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], "#@!321cba")
    
    def test_reverse_invalid_input_none(self):
        """Test reverse with None input."""
        result = reverse(None)
        self.assertEqual(result["status"], "error")
        self.assertIsNone(result["result"])
    
    def test_reverse_invalid_input_int(self):
        """Test reverse with integer input."""
        result = reverse(12345)
        self.assertEqual(result["status"], "error")
        self.assertIsNone(result["result"])


class TestRemoveVowels(unittest.TestCase):
    """Test cases for remove_vowels function."""
    
    def test_remove_vowels_simple(self):
        """Test remove_vowels with simple string."""
        result = remove_vowels("hello")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], "hll")
    
    def test_remove_vowels_all_vowels(self):
        """Test remove_vowels with all vowels."""
        result = remove_vowels("aeiou")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], "")
    
    def test_remove_vowels_no_vowels(self):
        """Test remove_vowels with no vowels."""
        result = remove_vowels("bcdfg")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], "bcdfg")
    
    def test_remove_vowels_uppercase(self):
        """Test remove_vowels removes uppercase vowels."""
        result = remove_vowels("HELLO")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], "HLL")
    
    def test_remove_vowels_mixed_case(self):
        """Test remove_vowels with mixed case."""
        result = remove_vowels("HeLLo WoRLd")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], "HLL WRLd")
    
    def test_remove_vowels_with_spaces(self):
        """Test remove_vowels preserves spaces."""
        result = remove_vowels("hello world")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], "hll wrld")
    
    def test_remove_vowels_with_numbers(self):
        """Test remove_vowels with numbers and special chars."""
        result = remove_vowels("hello123world!@#")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], "hll123wrld!@#")
    
    def test_remove_vowels_empty_string(self):
        """Test remove_vowels with empty string."""
        result = remove_vowels("")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], "")
    
    def test_remove_vowels_invalid_input_none(self):
        """Test remove_vowels with None input."""
        result = remove_vowels(None)
        self.assertEqual(result["status"], "error")
        self.assertIsNone(result["result"])
    
    def test_remove_vowels_invalid_input_int(self):
        """Test remove_vowels with integer input."""
        result = remove_vowels(999)
        self.assertEqual(result["status"], "error")
        self.assertIsNone(result["result"])


if __name__ == "__main__":
    unittest.main()