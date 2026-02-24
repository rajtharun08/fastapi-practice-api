from app.core.db import enrollments_db

class EnrollmentRepository:
    def __init__(self):
        self.db = enrollments_db

    def enroll(self, enrollment_data: dict) -> dict:
        enrollment_data["id"] = len(self.db) + 1
        self.db.append(enrollment_data)
        return enrollment_data

    def get_all(self) -> list:
        return self.db

    def check_exists(self, student_id: int, course_id: int) -> bool:
        for entry in self.db:
            if entry["student_id"] == student_id and entry["course_id"] == course_id:
                return True
        return False

    def get_by_student(self, student_id: int) -> list:
        return [e for e in self.db if e["student_id"] == student_id]

    def get_by_course(self, course_id: int) -> list:
        return [e for e in self.db if e["course_id"] == course_id]