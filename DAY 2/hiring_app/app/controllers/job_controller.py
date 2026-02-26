from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.job_schema import JobCreate, JobResponse, JobUpdate
from app.repositories.job_repository import JobRepository
from app.services.job_service import JobService
from typing import List

router = APIRouter(prefix="/jobs", tags=["Jobs"])

def get_job_service(db: Session = Depends(get_db)):
    repo = JobRepository(db)
    return JobService(repo)

@router.post("/", response_model=JobResponse)
def create_job(job_data: JobCreate, service: JobService = Depends(get_job_service)):
    return service.create_job(job_data)

@router.get("/", response_model=List[JobResponse])
def read_jobs(skip: int = 0, limit: int = 10, service: JobService = Depends(get_job_service)):
    return service.get_jobs(skip=skip, limit=limit)

@router.put("/{job_id}", response_model=JobResponse)
def update_job(job_id: int, job_data: JobUpdate, service: JobService = Depends(get_job_service)):
    return service.update_job_details(job_id, job_data)