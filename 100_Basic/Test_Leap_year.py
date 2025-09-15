import unittest
from Leap_year import LeapYear


class TestLeapYear(unittest.TestCase):

    def test_divisible_by_400(self):
        self.assertTrue(LeapYear(2000).is_leap_year())
        self.assertTrue(LeapYear(2400).is_leap_year())

    def test_divisible_by_100_but_not_400(self):
        self.assertFalse(LeapYear(1900).is_leap_year())
        self.assertFalse(LeapYear(2100).is_leap_year())

    def test_divisible_by_4_but_not_100(self):
        self.assertTrue(LeapYear(2024).is_leap_year())
        self.assertTrue(LeapYear(1996).is_leap_year())

    def test_not_divisible_by_4(self):
        self.assertFalse(LeapYear(2023).is_leap_year())
        self.assertFalse(LeapYear(1997).is_leap_year())

    def test_invalid_input_zero_or_negative(self):
        with self.assertRaises(ValueError):
            LeapYear(0)
        with self.assertRaises(ValueError):
            LeapYear(-10)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            LeapYear("2024")


if __name__ == "__main__":
    unittest.main()
