from app.repositories.application_repository import ApplicationRepository
from app.repositories.job_repository import JobRepository
from app.repositories.user_repository import UserRepository
from app.schemas.application_schema import ApplicationCreate
from app.exceptions.custom_exceptions import JobNotFoundException,UserAlreadyExistsException
from fastapi import HTTPException

class ApplicationService:
    def __init__(
        self, app_repo: ApplicationRepository, job_repo: JobRepository, user_repo: UserRepository):
        self.app_repo = app_repo
        self.job_repo = job_repo
        self.user_repo = user_repo

    def submit_application(self, application_data: ApplicationCreate):
        if not self.job_repo.get_by_id(application_data.job_id):
            raise JobNotFoundException()
        
        if not self.user_repo.get_by_id(application_data.user_id):
            raise UserAlreadyExistsException()
        
        return self.app_repo.create(application_data)