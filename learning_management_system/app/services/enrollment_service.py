from fastapi import HTTPException

class EnrollmentService:
    def __init__(self, enrollment_repository, student_repository, course_repository):
        self.enrollment_repository = enrollment_repository
        self.student_repository = student_repository
        self.course_repository = course_repository

    def enroll_student(self, enrollment_data):
        if not self.student_repository.get_by_id(enrollment_data.student_id):
            raise HTTPException(status_code=404, detail="Student not found")

        if not self.course_repository.get_by_id(enrollment_data.course_id):
            raise HTTPException(status_code=404, detail="Course not found")
        if self.enrollment_repository.check_exists(enrollment_data.student_id, enrollment_data.course_id):
            raise HTTPException(status_code=400, detail="Already enrolled")

        return self.enrollment_repository.enroll(enrollment_data.model_dump())

    def get_all_enrollments(self):
        return self.enrollment_repository.get_all()
    
    def get_student_enrollments(self, student_id: int):
        enrollments = self.enrollment_repository.get_by_student(student_id)
        results = []
        for e in enrollments:
            course = self.course_repository.get_by_id(e["course_id"])
            results.append({
                "course_id": e["course_id"],
                "course_title": course["title"] if course else "Unknown"
            })
        return results