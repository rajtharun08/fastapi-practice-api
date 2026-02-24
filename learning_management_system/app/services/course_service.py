from fastapi import HTTPException

class CourseService:
    def __init__(self,course_repository):
        self.course_repository=course_repository

    def create_course(self,course_data):
        return self.course_repository.create(course_data.model_dump())
    def get_all_courses(self):
        return self.course_repository.get_all()
    def get_course_by_id(self, course_id: int):
        course = self.course_repository.get_by_id(course_id)
        if not course:
            raise HTTPException(status_code=404, detail="Course not found") 
        return course