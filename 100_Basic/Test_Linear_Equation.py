import unittest
from Linear_equation import LinearEquation


class TestLinearEquation(unittest.TestCase):

    def test_solve_positive_a(self):
        equation = LinearEquation(2, 4)  # 2x + 4 = 0
        self.assertEqual(equation.calculate(), -2)

    def test_solve_negative_a(self):
        equation = LinearEquation(-5, 10)  # -5x + 10 = 0
        self.assertEqual(equation.calculate(), 2)

    def test_solve_with_float(self):
        equation = LinearEquation(0.5, 1.5)  # 0.5x + 1.5 = 0
        self.assertEqual(equation.calculate(), -3)

    def test_a_cannot_be_zero(self):
        with self.assertRaises(ValueError):
            LinearEquation(0, 5)


if __name__ == "__main__":
    unittest.main()
