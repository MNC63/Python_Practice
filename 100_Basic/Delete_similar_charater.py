"""
Find and delete similar character
"""


class UniqueCharacterFinder:
    """A class to find and delete similar character"""

    def __init__(self, text: str):
        self.text = list(text.replace(" ", ""))

    def get_unique_chars(self) -> list:
        """Find and add unique characters into list"""
        unique_chars = []
        for i in self.text:
            if i not in unique_chars:
                unique_chars.append(i)
        return unique_chars


def main():
    text_input = input("Enter characters separate by space: ")
    unique = UniqueCharacterFinder(text_input)
    print(f"The list have unique characters: {unique.get_unique_chars()}")


if __name__ == "__main__":
    main()
