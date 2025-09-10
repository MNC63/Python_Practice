""" 
Tinh giai thua cua mot so nguyen duong
"""


class Factorial:

    def __init__(self, number: int):
        if number < 0:
            raise ValueError("n phai la so nguyen duong")
        self.number = number

    def calculate_factorial(self) -> int:
        result = 1
        for i in range(1, self.number + 1):
            result *= i
        return result


def main():
    n = int(input("Nhap vao so muon tinh giai thua: "))
    calc = Factorial(n)
    print(f'Giai thua cua {n} bang : {calc.calculate_factorial()}')


if __name__ == "__main__":
    main()
