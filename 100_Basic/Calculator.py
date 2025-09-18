"""
Calculator basic with four operators
"""

from abc import ABC, abstractmethod  # import abc - Abstract Base Class


class Operation(ABC):
    @abstractmethod
    def calculate(self, a: float, b: float) -> float:
        pass


class AddOperation(Operation):
    def calculate(self, a, b):
        return a + b


class SubtractOperation(Operation):
    def calculate(self, a, b):
        return a - b


class MultiplyOperation(Operation):
    def calculate(self, a, b):
        return a * b


class DivideOperation(Operation):
    def calculate(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Can not divide by zero")
        return a / b


def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Choose operation (+, -, *, /): ")

        # Map user input to the correct strategy:
        strategies = {
            "+": AddOperation(),
            "-": SubtractOperation(),
            "*": MultiplyOperation(),
            "/": DivideOperation()
        }

        if op not in strategies:
            raise ValueError("Invalid operator")

        strategy = strategies[op]  # select strategy
        result = strategy.calculate(a, b)
        print(f"Result: {result}")

    except ValueError as e:
        print(f"Input error: {e}")
    except ZeroDivisionError as e:
        print(f"Math error: {e}")


if __name__ == "__main__":
    main()
