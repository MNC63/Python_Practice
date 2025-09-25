"""
Sort character in list
"""


class SortCharacter:
    """A class to sort all character in list"""

    def __init__(self, text: str):
        self.text = list(text.replace(" ", ""))

    def get_unique_chars(self) -> list:
        """Find and add unique characters into list"""
        unique_chars = []
        for i in self.text:
            if i not in unique_chars:
                unique_chars.append(i)
        return unique_chars

    def get_sort(self) -> list:
        return sorted(self.get_unique_chars())

    def get_sort_reverse(self) -> list:
        return sorted(self.get_unique_chars(), reverse=True)


def main():
    text_input = input("Enter the text: ")
    sort_character = SortCharacter(text_input)
    print(f"The sort characters list: {sort_character.get_sort()}")
    print(
        f"The reverse sort characters list: {sort_character.get_sort_reverse()}")


if __name__ == "__main__":
    main()
