"""
Countdown timer
"""

import time


class Clock:
    """A class to write a simple countdown timer"""

    def __init__(self, seconds: int):
        if seconds < 0:
            raise ValueError("Time must be a non-negative integer")
        self.seconds = seconds

    def countdown(self):
        while self.seconds > 0:
            mins, secs = divmod(self.seconds, 60)
            timer = f"{mins:02}:{secs:02}"
            print(timer, end="\r")
            time.sleep(1)
            self.seconds -= 1
        print("00:00")
        print("⏰ Time's up!")


def main():
    try:
        total_seconds = int(input("Enter countdown time (in seconds): "))
        clock = Clock(total_seconds)
        clock.countdown()
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
