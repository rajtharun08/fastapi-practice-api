from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.student_repository import StudentRepository
from app.repositories.course_repository import CourseRepository
from fastapi import HTTPException

class EnrollmentService:
    def __init__(
        self, 
        enrollment_repo: EnrollmentRepository,
        student_repo: StudentRepository,
        course_repo: CourseRepository
    ):
        self.enrollment_repo = enrollment_repo
        self.student_repo = student_repo
        self.course_repo = course_repo

    def enroll_student(self, student_id: int, course_id: int):
        if not self.student_repo.get_by_id(student_id):
            raise HTTPException(status_code=404, detail="Student not found") 
        
        if not self.course_repo.get_by_id(course_id):
            raise HTTPException(status_code=404, detail="Course not found") 

        if self.enrollment_repo.check_exists(student_id, course_id):
            raise HTTPException(status_code=400, detail="Already enrolled")

        return self.enrollment_repo.enroll({"student_id": student_id, "course_id": course_id})

    def get_all_enrollments(self):
        return self.enrollment_repo.get_all()

    def get_student_enrollments(self, student_id: int):
        if not self.student_repo.get_by_id(student_id):
            raise HTTPException(status_code=404, detail="Student not found")
            
        enrollments = self.enrollment_repo.get_by_student(student_id)
        
        result = []
        for enrollment in enrollments:
            course = self.course_repo.get_by_id(enrollment.course_id)
            result.append({
                "course_id": course.id,
                "course_title": course.title
            })
        return result