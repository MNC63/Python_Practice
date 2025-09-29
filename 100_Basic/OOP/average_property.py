"""
Calculate average grade of Physic, Math and English
"""


class Average:

    def __init__(self, name: str, **grades: float):
        self.name = name
        self._grades = {}
        for subject, value in grades.items():
            self.set_grade(subject, value)

    def set_grade(self, subject: str, value: float) -> None:
        """Set a grade for a subject with validation"""
        if not 0 <= value <= 100:
            raise ValueError(f"{subject} grade must be between 0 and 100")
        self._grades[subject] = value

    def get_grade(self, subject: str) -> float:
        """Retrieve grade for a subject"""
        return self._grades.get(subject, None)

    @property
    def grades(self) -> dict:
        """copy grade - read only"""
        return dict(self._grades)

    def get_average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self._grades.values()) / len(self._grades)

    def __str__(self):
        subjects = ", ".join(f"{sub}: {val}" for sub,
                             val in self._grades.items())
        return (f"Student: {self.name}\n"
                f"Grade -> {subjects}\n"
                f"Average: {self.get_average():.2f} points"

                )


def main():
    name = input("Enter Student's name: ")

    student = Average(
        name,
        physics=float(input("Enter Physics grade: ")),
        math=float(input("Enter Math grade: ")),
        english=float(input("Enter English grade: ")),
        chemistry=float(input("Enter Chemistry grade: "))
    )

    print(student)


if __name__ == "__main__":
    main()
