"""
Count characters in a given string
"""


class Count:

    def __init__(self, text: str):
        self.text = text

    def count_character(self) -> dict:
        counts = {}
        for char in self.text:
            counts[char] = counts.get(char, 0) + 1
        return counts


def main():
    user_input = input("Enter a string: ")
    count = Count(user_input)
    result = count.count_character()
    print("Character count: ")
    for char, count in result.items():
        print(f"'{char}': {count}")


if __name__ == "__main__":
    main()
