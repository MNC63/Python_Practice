"""
Check a character is vowel
"""


class VowelChecker:
    """Class to check if a single character is a vowel"""

    def __init__(self, char: str):
        if len(char) != 1:
            raise ValueError("character must be single")
        self.char = char.lower()

    def is_vowel(self) -> bool:
        vowels = "aeiou"
        return self.char in vowels


def main():
    try:
        char_input = input("Enter the character: ").lower()
        vowels = VowelChecker(char_input)
        print(f"{char_input} is Vowel: {vowels.is_vowel()}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
