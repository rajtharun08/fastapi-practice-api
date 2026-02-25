from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.application_schema import ApplicationCreate, ApplicationResponse
from app.repositories.application_repository import ApplicationRepository
from app.repositories.job_repository import JobRepository
from app.repositories.user_repository import UserRepository
from app.services.application_service import ApplicationService

router = APIRouter(prefix="/applications", tags=["Applications"])

def get_app_service(db: Session = Depends(get_db)):
    app_repo = ApplicationRepository(db)
    job_repo = JobRepository(db)
    user_repo = UserRepository(db)
    return ApplicationService(app_repo, job_repo, user_repo)

@router.post("/", response_model=ApplicationResponse)
def apply_to_job(app_data: ApplicationCreate, service: ApplicationService = Depends(get_app_service)):
    return service.submit_application(app_data)