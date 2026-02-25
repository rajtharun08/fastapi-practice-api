from app.repositories.job_repository import JobRepository
from app.schemas.job_schema import JobCreate, JobUpdate
from fastapi import HTTPException
from app.exceptions.custom_exceptions import JobNotFoundException
class JobService:
    def __init__(self, repository: JobRepository):
        self.repository = repository

    def create_job(self, job_data: JobCreate):
        return self.repository.create(job_data)

    def get_jobs(self, skip: int = 0, limit: int = 10):
        return self.repository.get_all(skip=skip, limit=limit)

    def update_job_details(self, job_id: int, job_data: JobUpdate):
        job = self.repository.update(job_id, job_data)
        if not job:
            raise JobNotFoundException()  
        return job