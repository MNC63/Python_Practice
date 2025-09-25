"""
Get prime in list
"""
import math


class Prime:
    """A class to get all prime in list"""

    def __init__(self, data: list):
        self.data = data

    @staticmethod
    def is_prime(n: int) -> bool:
        """Check a number is prime"""
        if n < 2:
            return False
        return all(n % i != 0 for i in range(2, int(math.sqrt(n) + 1)))

    def get_integer(self) -> list:
        """Return only integers from data"""
        return [x for x in self.data if isinstance(x, int)]

    def get_prime(self) -> list:
        return [n for n in self.get_integer() if self.is_prime(n)]


def main():
    list1 = [3, 5.6, "a", 5, 8, 10, -7, 0, 1, 11]
    prime = Prime(list1)
    print(f"Prime in list: {prime.get_prime()}")


if __name__ == "__main__":
    main()
