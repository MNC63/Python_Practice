from dataclasses import dataclass
import math

# @dataclass
# class Student:
#     name: str
#     age: int = 18
#     gpa: float = 1.0


# s1 = Student("Nhu", 24, 3.5)
# s2 = Student("Loc", 25, 2.7)

# print(f"{s1.name} loves {s2.name}")

@dataclass
class PrimeChecker:
    number: int

    def is_prime(self) -> bool:
        n = self.number
        if n <= 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def show_result(self):
        if self.is_prime():
            print(f"{self.number} is a prime number")
        else:
            print(f"{self.number} is not a prime number")


n = int(input("Enter a number: "))
checker = PrimeChecker(n)
checker.show_result()
