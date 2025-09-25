"""
Connect two lists
"""
from itertools import chain
from dataclasses import dataclass
from typing import Any


@dataclass
class Connection:
    """A class to connect lists"""
    list1: list[Any]
    list2: list[Any]

    def get_connection(self) -> list:
        """Return new list that is the connection of first list and second list"""
        return list(chain(self.list1, self.list2))


def main():
    ls_1 = [1, 2, 3]
    ls_2 = [4, 5, 6]
    connection = Connection(ls_1, ls_2)
    print(f"The connected list is: {connection.get_connection()}")


if __name__ == "__main__":
    main()
