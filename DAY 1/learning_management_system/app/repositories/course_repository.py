from app.core.db import courses_db
from app.models.course_model import Course

class CourseRepository:
    def __init__(self):
        self.db=courses_db
        
    def create(self,course_data:dict)->Course:
        id1=id=len(self.db)+1
        new_course=Course(
            id=id1,
            title=course_data["title"],
            duration=course_data["duration"]
        )
        self.db.append(new_course)
        return new_course
    
    def get_all(self)->list:
        return self.db

    def get_by_id(self,course_id:int)->Course | None:
        for course in self.db:
            if course.id==course_id:
                return course
        return None