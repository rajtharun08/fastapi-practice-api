from fastapi import APIRouter, Depends
from app.schemas.course_schema import CourseCreate, CourseResponse
from app.services.course_service import CourseService
from app.dependencies.dependencies import get_course_service
from typing import List

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.post("/", response_model=CourseResponse, status_code=201)
def create_course(course_data: CourseCreate, service: CourseService = Depends(get_course_service)):
    return service.create_course(course_data)
@router.get("/", response_model=List[CourseResponse])
def get_courses(service: CourseService = Depends(get_course_service)):
    return service.get_all_courses()
@router.get("/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, service: CourseService = Depends(get_course_service)):
    return service.get_course_by_id(course_id)