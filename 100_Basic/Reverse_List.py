"""
Reverse a string entered by the user
"""


class Reverse:

    def __init__(self, text: str):
        self.text = text

    def reverse(self) -> str:
        return self.text[::-1]


def main():
    enter_text = input("Nhap vao chuoi: ")
    res = Reverse(enter_text)
    print(f"Chuoi dao nguoc: {res.reverse()}")


if __name__ == "__main__":
    main()
