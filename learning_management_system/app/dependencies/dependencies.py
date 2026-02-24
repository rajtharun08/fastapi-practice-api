from app.repositories.student_repository import StudentRepository
from app.repositories.course_repository import CourseRepository
from app.repositories.enrollment_repository import EnrollmentRepository
from app.services.student_service import StudentService
from app.services.course_service import CourseService
from app.services.enrollment_service import EnrollmentService

student_repo = StudentRepository()
course_repo = CourseRepository()
enrollment_repo = EnrollmentRepository()

student_serv = StudentService(student_repo)
course_serv = CourseService(course_repo)
enrollment_serv = EnrollmentService(enrollment_repo, student_repo, course_repo)

def get_student_service():
    return student_serv

def get_course_service():
    return course_serv

def get_enrollment_service():
    return enrollment_serv