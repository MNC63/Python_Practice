"""
Find the number that is second greatest in list
"""


class SecondNum:
    """A class to get number that have second greatest value """

    def __init__(self, nums: dict):
        self.nums = nums

    def get_sort(self):
        sorted_items = sorted(
            self.nums.items(), key=lambda item: item[1], reverse=True)
        return sorted_items[1]


def main():
    data = {"b": 3, "a": 1, "c": 2, "f": 10}
    obj = SecondNum(data)
    key, value = obj.get_sort()
    print(
        f"The number has second greatest value that is {key} with value: {value}")


if __name__ == "__main__":
    main()
