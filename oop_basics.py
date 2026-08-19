"""Python OOP Basics — classes, objects, attributes, and methods.

A minimal, well-commented introduction to object-oriented programming:
- a class as a blueprint
- class attributes (shared) vs instance attributes (per object)
- instance methods
- a readable string representation via __str__
"""


class Student:
    """A simple model of a student."""

    school = "Governor House"  # class attribute — shared by every instance

    def __init__(self, name, marks):
        self.name = name        # instance attributes — unique to each object
        self.marks = list(marks)

    def average(self):
        """Return the average of the student's marks (0 if none)."""
        return sum(self.marks) / len(self.marks) if self.marks else 0.0

    def __str__(self):
        return f"{self.name} - average {self.average():.1f}"


def main():
    students = [
        Student("Ayesha", [90, 85, 88]),
        Student("Bilal", [70, 75, 80]),
    ]
    for student in students:
        print(student)
        print(f"  School: {Student.school}")


if __name__ == "__main__":
    main()
