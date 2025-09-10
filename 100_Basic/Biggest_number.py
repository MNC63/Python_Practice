"""
Find biggest and smallest number in three numbers
"""


class BN:

    def __init__(self, numbers: list[float]):
        self.numbers = numbers

    def check_biggest(self) -> float:
        b_number = self.numbers[0]
        for _, value in enumerate(self.numbers):
            if value > b_number:
                b_number = value
        return b_number

    def check_smallest(self) -> float:
        s_number = self.numbers[0]
        for _, value in enumerate(self.numbers):
            if value < s_number:
                s_number = value
        return s_number


def main():
    input_user = input("Enter three numbers (seperated by space): ")
    numbers = [int(x) for x in input_user.split()]
    bn = BN(numbers)
    print(f"The biggest number is {bn.check_biggest()}")
    print(f"The smallest number is {bn.check_smallest()}")


if __name__ == "__main__":
    main()
