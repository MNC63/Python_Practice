"""
Convert Decimal number into Binary number
"""


class ConvertDecimal:
    """Class to convert Decimal number into Binary number"""

    def __init__(self, n: int):
        if n < 0:
            raise ValueError("n must be a non-negative integer")
        self.n = n

    def decimal_to_binary(self) -> str:
        result = ""
        num = self.n
        if num == 0:
            return "0"
        while num > 0:
            result = str(num % 2) + result
            num //= 2
        return result


def main():
    try:
        num = int(input("Enter the number: "))
        convert = ConvertDecimal(num)
        print(f"The binary number of {num} is: {convert.decimal_to_binary()}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
