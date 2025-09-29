"""
Convert array into array 2D
"""
from typing import List


class Array2D:
    """A class to convert array into array 2D"""

    def __init__(self, arr: List[int], rows: int, cols: int):
        if rows <= 0 or cols <= 0:
            raise ValueError("Rows and Cols must be greater than zero")
        if rows * cols != len(arr):
            raise ValueError("rows * cols must equal length of array")
        self.arr = arr
        self.rows = rows
        self.cols = cols

    def get_convert(self):
        """Return array with cols and rows"""
        return [self.arr[i:i+self.cols] for i in range(0, len(self.arr), self.cols)]
        # for i in range (0, lens(self.arr), self.cols):
        #   return [self.arr[ i : i + self.cols ]]

    def display(self):
        arr_2d = self.get_convert()
        print("Array 2D:")
        for row in arr_2d:
            print(row)


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rows, cols = 3, 3
    array = Array2D(arr, rows, cols)
    array.display()


if __name__ == "__main__":
    main()
