"""
Create a dictionary from value and key what is given
"""


class Dictionary:
    """A class to create a new dictionary"""

    def __init__(self, keys: list, values: list):
        if len(keys) != len(values):
            raise ValueError("Keys and values must have the same length")
        self.keys = keys
        self.values = values

    def zip_dictionary(self) -> dict:
        return {k: v for k, v in zip(self.keys, self.values)}

    def display(self):
        print(f"New dictionary: {self.zip_dictionary()}")


def main():
    keys = ["a", "b", "c"]
    values = [1, 2, 5]

    try:
        dic = Dictionary(keys, values)
        dic.display()
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
