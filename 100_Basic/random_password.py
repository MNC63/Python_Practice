"""
Get random password from given character
"""

import random


class Password:
    """Generate random password of n characters from a given set characters """

    def __init__(self, text: str, length: int):
        if length <= 0:
            raise ValueError("length must be a number greater than zero")
        if len(text) == 0:
            raise ValueError("Random password must enter character")
        self.text = list(dict.fromkeys(text))
        self.length = length

    def get_random_password(self):
        # if self.length > len(self.clean_text()):
        #     raise ValueError(
        #         "Password length exceed number of unique characters")
        return random.choices(self.text, k=self.length)

    def print_password(self) -> str:
        password = "".join(self.get_random_password())
        print(f"Password: {password}")


def main():
    input_text = input("Enter the character for random: ")
    input_length = int(input("Enter the length of password: "))
    try:
        password = Password(input_text, input_length)
        password.print_password()
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
