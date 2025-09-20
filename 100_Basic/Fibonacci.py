"""
Print Fibonacci
"""


class Fibonacci:

    def __init__(self, num: int):
        if num < 0:
            raise ValueError("num must be a non-negative integer")
        self.num = num

    def calculate(self) -> list[int]:
        """Calculate Fibonacci of a number"""
        return [self._recursive(i) for i in range(self.num + 1)]

    def _recursive(self, k: int) -> int:
        if k == 0:
            return 0
        if k == 1:
            return 1
        return self._recursive(k - 1) + self._recursive(k - 2)


def main():
    try:
        num = int(input("Enter the number: "))
        fibonacci = Fibonacci(num)
        sequence = fibonacci.calculate()
        print(f"Fibonacci sequence up to {num}: {sequence}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
