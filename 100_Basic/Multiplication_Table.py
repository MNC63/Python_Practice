"""
print Multiplication Table from a number to a number
"""


class Multiplication:
    def __init__(self, start: int = 2, end: int = 9):
        if start < 1 or end < 1:
            raise ValueError("Cac so phai la so nguyen duong")
        if end < start:
            raise ValueError("So bat dau phai nho hon so ket thuc")
        self.start = start
        self.end = end

    def print_table(self) -> None:
        for n in range(self.start, self.end + 1):
            print(f"Bang cuu chuong cua {n} la: ")
            for i in range(1, 11):
                print(f"{n} x {i} = {n * i}")


def main():
    start_number = int(input("Nhap vao so dau: "))
    end_number = int(input("Nhap vao so cuoi: "))
    mult = Multiplication(start_number, end_number)
    mult.print_table()


if __name__ == "__main__":
    main()
