"""
Find the items which have most occurrences in string
"""
from collections import Counter


class CommonItems:
    """A Class using counter to find common items in list"""

    def __init__(self, words: str):
        self.words = words

    def get_common_items(self) -> dict:
        counter = Counter(self.words)
        return counter.most_common(1)[0]


def main():
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    counter = CommonItems(words)
    print(f"The most common character is: {counter.get_common_items()}")


if __name__ == "__main__":
    main()
