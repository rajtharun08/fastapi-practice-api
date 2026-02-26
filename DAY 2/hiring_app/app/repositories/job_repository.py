from sqlalchemy.orm import Session
from app.models.job import Job
from app.schemas.job_schema import JobCreate, JobUpdate

class JobRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, job: JobCreate):
        db_job = Job(**job.model_dump())
        self.db.add(db_job)
        self.db.commit()
        self.db.refresh(db_job)
        return db_job

    def get_by_id(self, job_id: int):
        return self.db.query(Job).filter(Job.id == job_id).first()

    def get_all(self, skip: int = 0, limit: int = 10):
        return self.db.query(Job).offset(skip).limit(limit).all()

    def update(self, job_id: int, job_data: JobUpdate):
        db_job = self.get_by_id(job_id)
        if db_job:
            update_data = job_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_job, key, value)
            self.db.commit()
            self.db.refresh(db_job)
        return db_job

    def delete(self, job_id: int):
        db_job = self.get_by_id(job_id)
        if db_job:
            self.db.delete(db_job)
            self.db.commit()
            return True
        return False