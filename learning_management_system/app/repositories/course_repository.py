from app.core.db import courses_db

class CourseRepository:
    def __init__(self):
        self.db=courses_db
        
    def create(self,course_data:dict)->dict:
        course_data["id"]=len(self.db)+1
        self.db.append(course_data)
        return course_data
    
    def get_all(self)->list:
        return self.db

    def get_by_id(self,course_id:int)->dict:
        for course in self.db:
            if course["id"]==course_id:
                return course
        return None