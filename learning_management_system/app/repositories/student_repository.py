from app.core.db import students_db

class StudentRepository:
    def __init__(self):
        self.db = students_db

    def create(self, student_data: dict) -> dict:
        student_data["id"] = len(self.db) + 1
        self.db.append(student_data)
        return student_data

    def get_by_id(self, student_id: int) -> dict:
        for student in self.db:
            if student["id"] == student_id:
                return student
        return None

    def get_by_email(self, email: str) -> dict:
        for student in self.db:
            if student["email"] == email:
                return student
        return None