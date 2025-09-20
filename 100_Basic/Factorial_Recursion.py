"""
Definition: n! = n * (n-1) * (n-2) .... 1
Recursion: fact(n) = {
            1,              n = 0 or n =1
            n * fact(n-1),  n > 1 
}
"""


class Factorial:
    """A class to calculate factorial of an integer number """

    def __init__(self, n: int):
        if n < 0:
            raise ValueError("n must be positive")
        self.n = n

    def calculate(self) -> int:
        """Calculate factorial of number"""
        return self._recursive(self.n)

    def _recursive(self, k: int) -> int:
        """Private recursive"""
        if k in (0, 1):
            return 1
        return k * self._recursive(k - 1)


def main():
    """Main function to execute calculate logic"""
    try:
        num = int(input("Enter the number: "))
        factorial = Factorial(num)
        print(f"The factorial of {num} = {factorial.calculate()}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
