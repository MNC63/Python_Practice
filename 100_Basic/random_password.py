"""
Get random password from given character
"""

import random


class Password:
    """A class to return password n characters that is random given characters """

    def __init__(self, text: str, length: int):
        if length <= 0:
            raise ValueError("length must be a number greater than zero")
        if len(text) == 0:
            raise ValueError("Random password must enter character")
        self.text = list(text)
        self.length = length

    def clean_text(self) -> list:
        """Return unique characters in text input"""
        cleaned = []
        for token in self.text:
            if token not in cleaned:
                cleaned.append(token)
        return cleaned

    def get_random_password(self):
        # if self.length > len(self.clean_text()):
        #     raise ValueError(
        #         "Password length exceed number of unique characters")
        return random.choices(self.clean_text(), k=self.length)

    def display(self):
        password = "".join(self.get_random_password())
        print(f"Password: {password}")


def main():
    input_text = input("Enter the character for random: ")
    input_length = int(input("Enter the length of password: "))
    try:
        password = Password(input_text, input_length)
        password.display()
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
