"""
Count the occurrences of words in str
"""


class CountOccurrences:

    def __init__(self, text: str):
        self.text = text

    def get_number_occ(self) -> list:
        word_counts = {}
        for word in self.text.split():
            word_counts.setdefault(word, 0)
            word_counts[word] += 1
        return word_counts


def main():
    text = input("Enter the sentence: ")
    occ = CountOccurrences(text)
    print(f"The occurrences of words in sentences: {occ.get_number_occ()}")


if __name__ == "__main__":
    main()
