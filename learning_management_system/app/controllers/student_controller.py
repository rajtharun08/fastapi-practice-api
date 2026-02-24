from fastapi import APIRouter, Depends
from app.schemas.student_schema import StudentCreate, StudentResponse
from app.dependencies.dependencies import get_student_service

router = APIRouter(prefix="/students")

@router.post("/", response_model=StudentResponse, status_code=201)
def register_student(student_data: StudentCreate, service=Depends(get_student_service)):
    return service.register_student(student_data)

@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, service=Depends(get_student_service)):
    return service.get_student_by_id(student_id)