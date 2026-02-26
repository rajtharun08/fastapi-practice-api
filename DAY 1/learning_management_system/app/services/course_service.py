from app.repositories.course_repository import CourseRepository
from app.schemas.course_schema import CourseCreate
from fastapi import HTTPException

class CourseService:
    def __init__(self, course_repo: CourseRepository):
        self.course_repo = course_repo
    def create_course(self, course_data: CourseCreate):
        return self.course_repo.create(course_data.model_dump())
    def get_all_courses(self):
        return self.course_repo.get_all()
    def get_course_by_id(self, course_id: int):
        course = self.course_repo.get_by_id(course_id)
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        return course