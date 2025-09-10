"""
Find Greatest Common Divisor and Least Common Multiple of two numbers
"""


class GDCLCM:

    def __init__(self, x: int, y: int):
        if x < 0 or y < 0:
            raise ValueError("Number must be non-negative")
        self.x = x
        self.y = y

    def calculate_gcd(self) -> int:
        a, b = self.x, self.y
        while b != 0:
            a, b = b, a % b
        return a

    def calculate_lcm(self) -> int:
        gcd_value = self.calculate_gcd()
        return 0 if gcd_value == 0 else (self.x * self.y) // gcd_value


def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    calc = GDCLCM(num1, num2)

    print(
        f"GCD of {num1} and {num2} is: {calc.calculate_gcd()}")
    print(
        f"LCM of {num1} and {num2} is: {calc.calculate_lcm()}")


if __name__ == "__main__":
    main()
