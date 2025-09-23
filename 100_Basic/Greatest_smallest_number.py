"""
Find the greatest and smallest number in list
"""


class GreatestSmallest:
    """A class to find the greatest and smallest number"""

    def __init__(self, number: str):
        self.numbers = []
        for token in number.split():
            try:
                self.numbers.append(float(token))
            except ValueError:
                raise ValueError(f"Invalid input: {token} is not a number")

    def get_greatest(self):
        return max(self.numbers)

    def get_smallest(self):
        return min(self.numbers)


def main():
    try:
        input_str = input("Enter numbers separate by space: ")
        gsn = GreatestSmallest(input_str)
        print(f"The greatest is: {gsn.get_greatest()}")
        print(f"The smallest is: {gsn.get_smallest()}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
