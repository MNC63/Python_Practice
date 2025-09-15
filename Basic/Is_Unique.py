"""
Is Unique: Implement an Algorithm to determine if a string has all characters
"""
import unittest


class Unique:

    def __init__(self, text: str):
        self.text = text

    def is_unique(self) -> bool:
        seen = {}
        for char in self.text:
            if char in seen:
                return False
            seen[char] = True
        return True


# ---------------------
# Unit Tests
# ---------------------

class TestUniqueChecker(unittest.TestCase):

    def test_unique_string(self):
        checker = Unique("abcdef")
        self.assertTrue(checker.is_unique())

    def test_non_unique_string(self):
        checker = Unique("anhyeuem")
        self.assertFalse(checker.is_unique())

    def test_empty_string(self):
        checker = Unique("")
        self.assertTrue(checker.is_unique())

    def test_single_char(self):
        checker = Unique("a")
        self.assertTrue(checker.is_unique())


if __name__ == "__main__":
    unittest.main()
