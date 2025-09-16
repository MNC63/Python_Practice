"""
Linear Equation
"""


class LinearEquation:
    def __init__(self, a: float, b: float):
        if a == 0:
            raise ValueError("a must not be zero")
        self.a = a
        self.b = b

    def calculate(self) -> float:
        return -self.b / self.a


def get_coefficients() -> tuple[float, float]:
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))


def main():
    a, b = get_coefficients()
    equation = LinearEquation(a, b)
    print(f"the result of linear equation is: {equation.calculate()}")


if __name__ == "__main__":
    main()
