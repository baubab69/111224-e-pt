class Student:
    def __init__(self, name: str, grades: list[int]):
        self.name = name
        self.grades = grades

    @classmethod
    def add_new_student(cls, name: str, grades: list[int]):
        return cls(name, grades)

    def __repr__(self) -> str:
        return f"Student(name={self.name}, grades={self.grades})"

    def __str__(self) -> str:
        return f"Student: {self.name}, Grades: {self.grades}"

def load_students_from_json(file_path: str) -> list[Student]:
    pass

def save_students_to_json(students: list[Student], file_path: str):
    pass

def main():
    # Your code here
    pass


if __name__ == '__main__':
    main()

