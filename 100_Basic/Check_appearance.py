"""
Check the appearance of an item in list 
"""
from typing import List


class Appearance:
    """A class to check the appearance of an item in list"""

    def __init__(self, data: List[str], key: str) -> None:
        self.data = data
        self.key = key

    def is_appearance(self) -> bool:
        return self.key in self.data


def main():
    items = ['anh', 'yeu', 'em']
    key = input("Enter the key: ")
    checker = Appearance(items, key)
    print(f"The appearance of {key} is: {checker.is_appearance()}")


if __name__ == "__main__":
    main()
