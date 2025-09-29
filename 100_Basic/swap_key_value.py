"""
Swap key and value in dictionary
"""


class Swapped:
    """A class to swap key and value position in dict"""

    def __init__(self, dicts: dict):
        self.dicts = dicts

    def get_swapped(self):
        swapped = {}
        for k, v in self.dicts.items():
            swapped.setdefault(v, []).append(k)
        return swapped

    def display(self):
        print(f"The swapped dict: {self.get_swapped()}")


def main():
    d = {"a": 1, "b": 1, "c": 2}
    swap = Swapped(d)
    swap.display()


if __name__ == "__main__":
    main()
