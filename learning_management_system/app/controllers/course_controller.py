from fastapi import APIRouter,Query,Depends
from typing import List
from app.services.course_service import CourseService
from app.schemas.course_schema import CourseResponse,CourseCreate
from app.dependencies.dependencies import get_course_service
router=APIRouter(prefix="/course")

@router.post("/",response_model=CourseResponse,status_code=201)
def create_course(course_data:CourseCreate,service=Depends(get_course_service)):
    return service.create_course(course_data)
@router.get("/", response_model=List[CourseResponse])
def list_courses(service=Depends(get_course_service)):
    return service.get_all_courses()

@router.get("/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, service=Depends(get_course_service)):
    return service.get_course_by_id(course_id)