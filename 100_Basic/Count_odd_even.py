"""
Count odd numbers and even numbers in a list
"""
import random


class CountOddEven:

    def __init__(self, numbers: list[float]):
        self.numbers = numbers
        self.odd = 0
        self.even = 0

    def count(self) -> int:
        for num in self.numbers:
            if num % 2 == 0:
                self.even += 1
            else:
                self.odd += 1

    def display(self):
        print(f"Number: {self.numbers}")
        print(f"Odd numbers: {self.odd}")
        print(f"Even number: {self.even}")


def main():
    numbers = [random.randint(1, 100) for _ in range(10)]
    count = CountOddEven(numbers)
    count.count()
    count.display()


if __name__ == "__main__":
    main()
