"""
Check perfect number
"""
import math


class PerfectNumber:
    """Class to check if a given number is perfect number"""

    def __init__(self, num: int):
        if num <= 0:
            raise ValueError("number must be positive")
        self.num = num

    def is_perfect(self) -> bool:
        """Return True if number is perfect, else False"""
        total = 1
        sqrt_n = int(math.sqrt(self.num))
        if self.num == 1:
            return False
        for i in range(2, sqrt_n + 1):
            if self.num % i == 0:
                pair = self.num // i

                if pair != i:
                    total += i

        return total == self.num


def main():
    """Main function to prompt user input and print result"""
    try:
        num = int(input("Enter the number: "))
        checker = PerfectNumber(num)

        if checker.is_perfect():
            print(f"{num} is a perfect number")
        else:
            print(f"{num} is NOT a perfect number")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
