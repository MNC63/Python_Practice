"""
Sort words that have length > n 
"""


class WordFilter:
    """A class to find words that have length greater than n"""

    def __init__(self, n: int, text: str):
        if n < 0:
            raise ValueError("n must be a non-negative integer")
        self.n = n
        self.text = text.split()

    def get_words(self) -> list:
        """Return a list that includes all words length greater than n """
        return [word for word in self.text if len(word) > self.n]


def main():
    text = input("Enter the sentence: ")
    n = int(input("Enter number n: "))

    try:
        filter = WordFilter(n, text)
        words = filter.get_words()
        print(f"Words with length greater than {n}: {words}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
