"""
Check leap year
"""


class LeapYear:
    def __init__(self, year: int):
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")
        if year <= 0:
            raise ValueError("Year must be a positive integer")
        self.year = year

    def is_leap_year(self) -> bool:
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        return self.year % 4 == 0


def main():
    try:
        year = int(input("Enter the year: "))
        leap_year = LeapYear(year)
        print(f"{year} is leap year: {leap_year.is_leap_year()}")
    except ValueError:
        print("Error: Please enter a positive integer for the year")
    except TypeError:
        print("Error: Year must be an integer")


if __name__ == "__main__":
    main()
