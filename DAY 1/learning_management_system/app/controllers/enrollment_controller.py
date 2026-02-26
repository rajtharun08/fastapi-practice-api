from fastapi import APIRouter, Depends
from app.schemas.enrollment_schema import EnrollmentCreate, EnrollmentResponse, StudentEnrollmentDetail
from app.services.enrollment_service import EnrollmentService
from app.dependencies.dependencies import get_enrollment_service
from typing import List

router = APIRouter(tags=["Enrollments"])

@router.post("/enrollments", response_model=EnrollmentResponse, status_code=201)
def enroll_student(data: EnrollmentCreate, service: EnrollmentService = Depends(get_enrollment_service)):
    return service.enroll_student(data.student_id, data.course_id)

@router.get("/enrollments", response_model=List[EnrollmentResponse])
def get_all_enrollments(service: EnrollmentService = Depends(get_enrollment_service)):
    return service.get_all_enrollments()

@router.get("/students/{student_id}/enrollments", response_model=List[StudentEnrollmentDetail])
def get_student_enrollments(student_id: int, service: EnrollmentService = Depends(get_enrollment_service)):
    return service.get_student_enrollments(student_id)