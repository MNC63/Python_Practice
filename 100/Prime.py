import math


def is_prime(n):
    if n < 2:
        print(f"{n} is not a prime number")
        return

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(f"{n} is not a prime number")
            return

    print(f"{n} is a prime number")


n = int(input("Enter a number:"))
is_prime(n)
