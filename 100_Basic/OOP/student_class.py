"""
Create student class that includes method: name, olds, grade
"""


class Student:

    def __init__(self, name: str, age: int, grade: float):
        self.name = name
        self.age = age
        self.grade = grade

    # --- age property ---
    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        if value < 0:
            raise ValueError("Age must be a non-negative number")
        self._age = value

    # --- grade property ---
    @property
    def grade(self) -> float:
        return self._grade

    @grade.setter
    def grade(self, value: float):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self._grade = value

    def __str__(self):
        return f"Student {self.name}, Age: {self.age}, Grade: {self.grade:.2f} points"


def main():

    # --- existing data ---
    students_data = [
        {"name": "Alice", "age": 20, "grade": 88.5},
        {"name": "Bob", "age": 22, "grade": 92.0},
        {"name": "Charlie", "age": 19, "grade": 76.3},
    ]

    students = [Student(**data) for data in students_data]

    # --- allow user to add more students ---
    while True:
        choice = input(
            "Do you want to add a new student? (y/n): ").strip().lower()
        if choice != "y":
            break
        try:
            name = input("Enter the name: ")
            age = int(input("Enter student's olds: "))
            grade = float(input("Enter student's grade: "))

            students.append(Student(name, age, grade))
            print("Student added successfully!\n")

        except ValueError as e:
            print(f"Error: {e}\n")
    print("\nAll Student:")
    for s in students:
        print(s)


if __name__ == "__main__":
    main()
