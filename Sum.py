# -------
# Variables
# -------
n = int(input("Enter a positive integer: "))
sum = 0

# -------
# Main
# -------


def calculate_sum(n):
    global sum
    for i in range(1, n + 1):
        sum += i
    print(f"The sum is {sum}")


calculate_sum(n)
