from app.repositories.student_repository import StudentRepository
from app.schemas.student_schema import StudentCreate
from fastapi import HTTPException

class StudentService:
    def __init__(self, student_repo: StudentRepository):
        self.student_repo = student_repo
    def register_student(self, student_data: StudentCreate):
        if self.student_repo.get_by_email(student_data.email):
            raise HTTPException(status_code=400, detail="Email already registered")
        return self.student_repo.create(student_data.model_dump())
    def get_student_by_id(self, student_id: int):
        student = self.student_repo.get_by_id(student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        return student