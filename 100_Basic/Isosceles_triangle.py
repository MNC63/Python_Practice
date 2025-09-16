"""
Print Isosceles Triangle
"""

from dataclasses import dataclass


@dataclass
class IsoscelesTriangle:
    n: int

    def __post_init__(self):
        if self.n < 1:
            raise ValueError("n must be greater than 1")

    def build(self) -> str:
        """Return the triangle as a single string"""
        return "\n".join(
            " " * (self.n - i - 1) + "*" * (2 * i + 1)
            for i in range(self.n)
        )

    def render(self) -> None:
        """Print the triangle to the console"""
        print(self.build())


def main():
    try:
        n = int(input("Enter a number greater than 1: "))
        isosceles = IsoscelesTriangle(n)
        isosceles.render()
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
