"""
Calculate the acreage of Circle and Rectangle
"""
import math


class Circle:
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be greater than zero")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle:
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and Height must be greater than zero")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def main():
    shape_type = input("Choose shape (circle/rectangle): ").strip().lower()
    try:
        if shape_type == "circle":
            r = float(input("Enter the radius: "))
            shape = Circle(r)
        elif shape_type == "rectangle":
            w = float(input("Enter the width: "))
            h = float(input("Enter the height: "))
            shape = Rectangle(w, h)
        else:
            print("Unknown shape")
            return

        print(f"Area: {shape.area():.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
