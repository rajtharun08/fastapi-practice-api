from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.application_schema import ApplicationCreate,ApplicationResponse,ApplicationUpdateStatus
from app.repositories.application_repository import ApplicationRepository
from app.repositories.product_repository import ProductRepository
from app.services.application_service import ApplicationService

router=APIRouter(prefix="/loan-applications",tags=["Applications"])
repo=ApplicationRepository()
p_repo=ProductRepository()
service=ApplicationService(repo,p_repo)

@router.post("/",response_model=ApplicationResponse)
def create(data:ApplicationCreate,db:Session=Depends(get_db)):
    return service.apply(db,data)

@router.get("/",response_model=list[ApplicationResponse])
def list_all(skip:int=0,limit:int=10,db:Session=Depends(get_db)):
    return service.list_applications(db,skip,limit)

@router.put("/{app_id}/status",response_model=ApplicationResponse)
def update_status(app_id:int,data:ApplicationUpdateStatus,db:Session=Depends(get_db)):
    return service.update_status(db,app_id,data)