"""
Print Multiplication Table of a number 
"""


class Multiplication:

    def __init__(self, n: int):
        if n < 0:
            raise ValueError("n phai la so tu nhien nguyen duong")
        self.n = n

    def print_table(self) -> None:
        for i in range(1, 11):
            print(f"{self.n} x {i} = {self.n * i}")


def main():
    number = int(input("Nhap so tu nhien tu 2 den 9: "))
    mult = Multiplication(number)
    print(f'Bang cuu chuong cua {number} la: ')
    mult.print_table()


if __name__ == "__main__":
    main()
