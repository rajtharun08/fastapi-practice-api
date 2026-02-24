from fastapi import APIRouter, Depends
from typing import List
from app.schemas.enrollment_schema import EnrollmentCreate, EnrollmentResponse, StudentEnrollmentDetail
from app.dependencies.dependencies import get_enrollment_service

router = APIRouter(prefix="/enrollments")

@router.post("/", response_model=EnrollmentResponse, status_code=201)
def enroll_student(enrollment_data: EnrollmentCreate, service=Depends(get_enrollment_service)):
    return service.enroll_student(enrollment_data)

@router.get("/", response_model=List[EnrollmentResponse])
def list_enrollments(service=Depends(get_enrollment_service)):
    return service.get_all_enrollments()

@router.get("/student/{student_id}", response_model=List[StudentEnrollmentDetail])
def get_student_courses(student_id: int, service=Depends(get_enrollment_service)):
    return service.get_student_enrollments(student_id)