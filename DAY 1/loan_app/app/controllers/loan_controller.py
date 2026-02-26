from fastapi import APIRouter,Depends
from app.dependencies.loan_dependency import get_loan_service
from app.schemas.loan_schema import LoanCreate,LoanResponse,LoanStatusUpdateResponse
from typing import List 

router=APIRouter(prefix="/loans",tags=["loans"])

@router.post("/",response_model=LoanResponse)
def apply(loan_data:LoanCreate,service=Depends(get_loan_service)):
    return service.apply_for_loan(loan_data)

@router.get("/{id}",response_model=LoanResponse)
def get_one(loan_id:int,service=Depends(get_loan_service)):
    return service.get_application_by_id(loan_id)

@router.get("/",response_model=List[LoanResponse])
def get_all(service=Depends(get_loan_service)):
    return service.get_all_applications()

@router.put("/{loan_id}/approve", response_model=LoanStatusUpdateResponse)
def approve(loan_id: int, service=Depends(get_loan_service)):
    return service.approve_loan(loan_id)

@router.put("/{loan_id}/reject", response_model=LoanStatusUpdateResponse)
def reject(loan_id: int, service=Depends(get_loan_service)):
    return service.reject_loan(loan_id)