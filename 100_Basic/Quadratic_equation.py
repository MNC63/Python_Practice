"""
Quadratic equation solver
"""
import math
from dataclasses import dataclass


@dataclass
class QuadraticEquation:
    """Class representing a quadratic equation: ax^2 + bx + c = 0"""
    a: float
    b: float
    c: float

    def __post_init__(self):
        if self.a == 0:
            raise ValueError("Coefficient 'a' must not be zero")

    def solve(self) -> list[float]:
        """Return a list of real roots of the equation."""
        delta = self.b ** 2 - 4 * self.a * self.c

        if delta > 0:
            sqrt_delta = math.sqrt(delta)
            return [(- self.b + sqrt_delta) / (2 * self.a),
                    (- self.b - sqrt_delta) / (2 * self.a)]
        elif delta == 0:
            return [self.b / (2 * self.a)]
        return []


def main():
    equation = QuadraticEquation(2, -4, -6)
    print(f"solution: {equation.solve()}")


if __name__ == "__main__":
    main()
