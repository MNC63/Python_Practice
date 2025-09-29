"""
Create a dict and count occurrence of character in list
"""


class Occurrences:
    """A class to count the occurrences of characters"""

    def __init__(self, data: list):
        self.data = data

    def get_occurrences(self):
        counts = dict.fromkeys(self.data, 0)
        for char in self.data:
            counts[char] += 1
        return counts

    def display(self):
        print(f"The occurrences of characters is: {self.get_occurrences()}")


def main():
    chars = ["a", "b", "a", "c", "b", "a"]
    occ = Occurrences(chars)
    occ.display()


if __name__ == "__main__":
    main()
