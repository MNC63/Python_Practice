"""
Get similar character in two lists
"""
from dataclasses import dataclass
from typing import Any


@dataclass
class DuplicatedChar:
    """A class to get all items which are the same between two lists"""

    list1: list[Any]
    list2: list[Any]

    def get_same_char(self) -> list[Any]:
        return list(set(self.list1) & set(self.list2))


def main():
    list1 = ['a', 'b', 'c', 'd']
    list2 = ['c', 'd', 'e', 'f']
    dup = DuplicatedChar(list1, list2)
    print(f"The same character are: {dup.get_same_char()}")


if __name__ == "__main__":
    main()
