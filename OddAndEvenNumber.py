import random

# -------
# Variables
# -------
results = []


# -------
# Main
# -------
for range in range(10):
    numbers = random.randint(1, 100)

    if numbers % 2 == 0:
        results.append((numbers, "Even"))
    else:
        results.append((numbers, "Odd"))

print(results)
