"""
Count words and character in lists
"""


class CountWordsChar:
    """A class to count words and characters in a string"""

    def __init__(self, text: str):
        self.text = text
        self.num_words = 0
        self.num_chars = 0

    def count(self) -> int:
        """Count words and characters in string"""
        text_split = self.text.split()
        self.num_words = len(text_split)
        self.num_chars = len(self.text)

    def display(self):
        """Display the results"""
        print(f"Text: {self.text}")
        print(f"Number of words: {self.num_words}")
        print(f"Number of Characters: {self.num_chars}")


def main():
    """Main function to execute counting logic"""
    text = input("Enter the sentence: ").strip()
    counts = CountWordsChar(text)
    counts.count()
    counts.display()


if __name__ == "__main__":
    main()
