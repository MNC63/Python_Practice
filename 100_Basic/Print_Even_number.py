"""
Create a list and print even numbers in list
"""


class PrintEvenNumber:
    """A class to print all even number in list"""

    def __init__(self, numbers: str):
        self.list_numbers = [int(x) for x in numbers.split()]

    def find_even_numbers(self) -> list:
        even_numbers = []
        if self.list_numbers == []:
            return []

        for i in self.list_numbers:
            if i % 2 == 0:
                even_numbers.append(i)
        return even_numbers


def main():
    list_number = input("Enter numbers separate by space: ")
    even = PrintEvenNumber(list_number)
    print(f"Even numbers in list are: {even.find_even_numbers()}")


if __name__ == "__main__":
    main()
