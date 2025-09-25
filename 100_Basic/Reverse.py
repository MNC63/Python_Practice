"""
Rotate array at k
"""


class Rotate:
    """A class to rotate array at k"""

    def __init__(self, arr: list, k: int):
        self.arr = arr
        self.k = k

    def rotate(self):
        k = self.k % len(self.arr)
        arr = self.arr

        # Step 1: reverse entire array
        arr.reverse()

        # Step 2: reverse first k
        arr[:k] = reversed(arr[:k])

        # Step 3: reverse the rest
        arr[k:] = reversed(arr[k:])

        return arr


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rotate = Rotate(arr, 3)
    print(rotate.rotate())


if __name__ == "__main__":
    main()
