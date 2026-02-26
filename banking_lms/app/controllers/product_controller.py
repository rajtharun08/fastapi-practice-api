from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.product_schema import ProductCreate,ProductResponse
from app.repositories.product_repository import ProductRepository
from app.services.product_service import ProductService

router=APIRouter(prefix="/loan-products",tags=["Products"])
repo=ProductRepository()
service=ProductService(repo)

@router.post("/",response_model=ProductResponse)
def create(product:ProductCreate,db:Session=Depends(get_db)):
    return service.create_product(db,product)

@router.get("/",response_model=list[ProductResponse])
def list_all(skip:int=0,limit:int=10,db:Session=Depends(get_db)):
    return service.list_products(db,skip,limit)