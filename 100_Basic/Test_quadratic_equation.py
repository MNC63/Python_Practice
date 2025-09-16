from Quadratic_equation import QuadraticEquation
import unittest


class TestQuadraticEquation(unittest.TestCase):

    def test_solve_delta_positive(self):
        equation = QuadraticEquation(2, -4, -6)
        self.assertEqual(equation.solve(), [3.0, -1.0])

    def test_solve_delta_zero(self):
        equation = QuadraticEquation(1, 2, 1)
        self.assertEqual(equation.solve(), [-1])

    def test_solve_delta_negative(self):
        equation = QuadraticEquation(5, 3, 5)
        self.assertEqual(equation.solve(), [])

    def test_a_cannot_be_zero(self):
        with self.assertRaises(ValueError):
            QuadraticEquation(0, 5, 7)


if __name__ == "__main__":
    unittest.main()
