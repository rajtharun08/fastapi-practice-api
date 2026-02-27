from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.controllers import auth_controller

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return auth_controller.login(db, form_data.username, form_data.password)