from pydantic import BaseModel
from typing import List, Optional

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

class EnrollmentResponse(BaseModel):
    id: int
    student_id: int
    course_id: int

    class Config:
        from_attributes = True

class StudentEnrollmentDetail(BaseModel):
    course_id: int
    course_title: str