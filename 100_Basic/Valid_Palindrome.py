"""
Check a str what's Palindrome?
"""


class Palindrome:

    def __init__(self, text: str):
        self.text = text

    def clean_text(self) -> str:
        return "".join(c.lower() for c in self.text if c.isalnum())

    def is_Palindrome(self) -> bool:
        cleaned = self.clean_text()
        return cleaned == cleaned[::-1]


def main():
    check = Palindrome("A man, A plan, A canal: panama")
    print(check.is_Palindrome())


if __name__ == "__main__":
    main()
