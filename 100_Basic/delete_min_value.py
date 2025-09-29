"""
Delete min key what have min value
"""


class DelMin:
    """A class to delete key that has min value in dict"""

    def __init__(self, data: dict):
        self.data = data

    def del_min(self):
        min_key = min(self.data, key=self.data.get)
        self.data.pop(min_key)
        return self.data

    def display(self):
        print(f"The result: {self.del_min()}")


def main():
    d = {"a": 5, "b": 2, "c": 3}
    obj = DelMin(d)
    obj.display()


if __name__ == "__main__":
    main()
