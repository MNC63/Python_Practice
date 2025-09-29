"""
Convert seconds to mins and hours
"""
import time


class HoursMinsSecs:
    """A class to convert hours mins and seconds"""

    def __init__(self, secs: int):
        if secs < 0:
            raise ValueError("Seconds must be a non-negative integer")
        self.secs = secs

    def get_time(self):
        mins, secs = divmod(self.secs, 60)
        hours, mins = divmod(mins, 60)
        return f"{hours:02}:{mins:02}:{secs:02}"

    def display(self):
        print(f"Time is: {self.get_time()}")


def main():
    secs = int(input("Enter the seconds: "))
    obj = HoursMinsSecs(secs)
    obj.display()


if __name__ == "__main__":
    main()
