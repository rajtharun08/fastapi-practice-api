from app.core.db import students_db
from app.models.student_model import Student
class StudentRepository:
    def __init__(self):
        self.db = students_db

    def create(self, student_data: dict) -> Student:
        id1=id=len(self.db)+1
        new_student = Student(
            id=id1,
            name=student_data["name"],
            email=student_data["email"]
        )
        self.db.append(new_student)
        return new_student

    def get_by_id(self, student_id: int) -> Student | None:
        for student in self.db:
            if student.id == student_id:
                return student
        return None

    def get_by_email(self, email: str) -> Student | None:
        for student in self.db:
            if student.email == email:
                return student
        return None