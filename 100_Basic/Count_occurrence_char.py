"""
Count the numbers of occurrence of characters in string
"""
from collections import Counter


class Occurrence:
    """Class to count the occurrence of every character"""

    def __init__(self, text: str):
        self.text = text

    def get_char_count(self) -> dict[str, int]:
        return dict(Counter(self.text))
        # occ = {}
        # # for char in self.text:
        # #     occ[char] = occ.get(char, 0) + 1
        # # return occ


def main():
    input_text = input("Enter the sentence: ").lower()
    occurrence = Occurrence(input_text)
    print(f"The result: {occurrence.get_char_count()}")


if __name__ == "__main__":
    main()
