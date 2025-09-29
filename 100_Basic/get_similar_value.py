"""
Find keys have similar value in dict
"""


class SimilarValue:
    """A class to find keys what have same value"""

    def __init__(self, data: dict):
        self.data = data

    def swap(self) -> dict:
        """Swap key and value in other to find keys that have same value"""
        swapped = {}
        for k, v in self.data.items():
            swapped.setdefault(v, []).append(k)
        return swapped

    def get_same_value(self) -> dict:
        """Return a new dict with value of keys is greater than 1"""
        return {val: keys for val, keys in self.swap().items() if len(keys) > 1}

    def display(self):
        print(f"The dict of keys have same value: {self.get_same_value()}")


def main():
    d = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
    sim = SimilarValue(d)
    sim.display()


if __name__ == "__main__":
    main()
