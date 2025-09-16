"""
Print Right Triangle
"""


class RightTriangle:

    def __init__(self, n: int):
        if n <= 1:
            raise ValueError("n must be greater than one")
        self.n = n

    def build(self) -> str:
        """Return the triangle as a single string"""
        return "\n".join("*" * (i + 1) for i in range(self.n))

    def render(self) -> None:
        """Print the triangle to the console"""
        print(self.build())


def main():
    try:
        n = int(input("Enter the number(greater 1): "))
        right_triangle = RightTriangle(n)
        right_triangle.render()
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
