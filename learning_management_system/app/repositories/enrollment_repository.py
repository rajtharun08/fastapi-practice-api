from app.core.db import enrollments_db
from app.models.enrollment_model import Enrollment
class EnrollmentRepository:
    def __init__(self):
        self.db = enrollments_db

    def enroll(self, enrollment_data: dict) -> Enrollment:
        id1=id=len(self.db)+1
        new_enrollment = Enrollment(
            id=id1,
            student_id=enrollment_data["student_id"],
            course_id=enrollment_data["course_id"]
        )
        self.db.append(new_enrollment)
        return new_enrollment

    def get_all(self) -> list:
        return self.db

    def check_exists(self, student_id: int, course_id: int) -> bool:
        for entry in self.db:
            if entry.student_id == student_id and entry.student_id == course_id:
                return True
        return False

    def get_by_student(self, student_id: int) -> list:
        return [e for e in self.db if e.student_id == student_id]

    def get_by_course(self, course_id: int) -> list:
        return [e for e in self.db if e.student_id == course_id]