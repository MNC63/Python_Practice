"""
Check a string is a palindrome
"""


class PalindromeChecker:
    """Class to check about palindrome of a string"""

    def __init__(self, text: str):
        self.text = text

    def clean_text(self) -> str:
        return " ".join(c.lower() for c in self.text if c.isalnum())

    def is_palindrome(self) -> bool:
        cleaned = self.clean_text()
        return cleaned == cleaned[::-1]


def main():

    checker1 = PalindromeChecker("A man, a plan, a canal: Panama")
    print(checker1.is_palindrome())

    checker2 = PalindromeChecker("race a car")
    print(checker2.is_palindrome())

    checker3 = PalindromeChecker("")
    print(checker3.is_palindrome())


if __name__ == "__main__":
    main()
