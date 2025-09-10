"""
calculate average of all numbers
"""


class Average:

    def __init__(self, numbers: list[int]):
        self.numbers = numbers

    def calculate(self) -> float:
        total = sum(self.numbers)
        amount = len(self.numbers)
        return total / amount if amount != 0 else 0


def main():
    input_user = input("Enter a numbers's list (seperated by space): ")
    numbers = [int(x) for x in input_user.split()]
    average = Average(numbers)
    print(f"Sum of numbers is: {average.calculate()}")


if __name__ == "__main__":
    main()
