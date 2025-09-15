"""
Calculate the acreage of triangle
"""


class Triangle:

    def __init__(self, base: float, height: float):
        if base <= 0 or height <= 0:
            raise ValueError("Base and Height must be greater more zero")
        self.base = base
        self.height = height

    def calculate_acreage(self):
        return 0.5 * self.base * self.height


def main():
    try:
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        acreage_triangle = Triangle(base, height)
        print(
            f"The acreage of the triangle is: {acreage_triangle.calculate_acreage()}")
    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
