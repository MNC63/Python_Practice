"""
Find square numbers smaller number N
"""
import math


class SquareNumberFinder:
    """A class find all perfect square number up to a given limit (inclusive)"""

    def __init__(self, limit: int):
        if limit < 0:
            raise ValueError("Limit must be an positive integer")
        self.limit = limit

    def find(self) -> list[int]:
        """Return a list of perfect square number <= limit"""
        result = []
        for i in range(int(math.sqrt(self.limit)) + 1):
            result.append(i * i)
        return result


def main():
    try:
        num = int(input("Enter the integer number: "))
        finder = SquareNumberFinder(num)
        print(
            f"Square numbers are smaller than {num}: {finder.find()}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
