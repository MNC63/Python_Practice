"""
Calculate the sum of characters in list
"""


class CalculateSumChar:

    def __init__(self, num: str):
        self.num = num

    def calculate(self) -> int:
        sum = 0
        for index, value in enumerate(self.num):
            self.sum += int(value)
        return sum


def main():
    num = input("Enter number string: ")
    calculates_sum_char = CalculateSumChar(num)
    print(f"The sum is: {calculates_sum_char.calculate()}")


if __name__ == "__main__":
    main()
