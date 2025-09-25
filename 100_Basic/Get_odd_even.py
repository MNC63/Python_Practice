"""
Add odd and even numbers into two list
"""


class SeparateList:
    """A class to separate a list into odd and even lists"""

    def __init__(self, data: list):
        self.data = data
        self.even = [i for i in data if i % 2 == 0]
        self.odd = [i for i in data if i % 2 != 0]

    def display(self):
        print(f"The even numbers list: {self.even}")
        print(f"The odd numbers list: {self.odd}")


def main():
    list_input = [6, 8, 10, 5, -2]
    separate = SeparateList(list_input)
    separate.display()


if __name__ == "__main__":
    main()
