"""
Get keys and values in dictionary
"""


class GetKeyValue:
    """A class to get and return keys and value in dict"""

    def __init__(self, data: dict):
        self.data = data

    def get_average(self):
        return sum(self.data.values()) / len(self.data)

    def display(self):
        print(f"The average point is: {self.get_average()}")

        top_student = max(self.data, key=self.data.get)
        print(
            f"Top student: {top_student} with grade {self.data.get(top_student)}")


def main():
    students = {
        "Nhu": 85,
        "Loc": 90,
        "Tien": 50
    }
    getkv = GetKeyValue(students)
    getkv.display()


if __name__ == "__main__":
    main()
