from sqlalchemy.orm import Session
from app.models.application import Application
from app.schemas.application_schema import ApplicationCreate

class ApplicationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, application: ApplicationCreate):
        db_app = Application(**application.model_dump())
        self.db.add(db_app)
        self.db.commit()
        self.db.refresh(db_app)
        return db_app

    def get_by_id(self, app_id: int):
        return self.db.query(Application).filter(Application.id == app_id).first()

    def get_by_user(self, user_id: int):
        return self.db.query(Application).filter(Application.user_id == user_id).all()