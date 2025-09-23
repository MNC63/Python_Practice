"""
Calculate sum of all character in a list
"""


class NumberSummary:
    """A class to find summary of a list"""

    def __init__(self, number: str):
        self.list_numbers = []
        for x in number.split():
            try:
                self.list_numbers.append(float(x))
            except:
                raise ValueError(f"Invalid input: '{x}' is not a number.")

    def get_sum(self):
        return sum(self.list_numbers)


def main():
    try:
        list_num = input("Enter number list separate by space: ")
        num_summary = NumberSummary(list_num)
        print(f"The total is: {num_summary.get_sum()}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
