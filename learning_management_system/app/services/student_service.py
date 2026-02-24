from fastapi import HTTPException

class StudentService:
    def __init__(self, student_repository):
        self.student_repository = student_repository

    def register_student(self, student_data):
        if self.student_repository.get_by_email(student_data.email):
            raise HTTPException(status_code=400, detail="Email already registered")
        return self.student_repository.create(student_data.model_dump())

    def get_student_by_id(self, student_id: int):
        student = self.student_repository.get_by_id(student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        return student