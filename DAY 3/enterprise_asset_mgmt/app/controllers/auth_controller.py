from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories import user_repo
from app.services import auth_service

def login(db: Session, email: str, password: str):
    user = user_repo.get_user_by_email(db, email)
    if not user or not auth_service.verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    access_token = auth_service.create_access_token(data={"sub": user.email, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}