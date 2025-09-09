"""Given a string, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases
"""


class PalindromeChecker:

    def __init__(self, text: str):
        self.text = text

    def _clean_text(self) -> str:
        return "".join(c.lower() for c in self.text if c.isalnum())

    def is_palindrome(self) -> bool:
        cleaned = self._clean_text()
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
