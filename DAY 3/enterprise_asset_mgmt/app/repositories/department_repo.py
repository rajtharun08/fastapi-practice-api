from sqlalchemy.orm import Session
from app.models.department import Department

def get_all_departments(db: Session):
    return db.query(Department).all()

def get_department_by_id(db: Session, dept_id: int):
    return db.query(Department).filter(Department.id == dept_id).first()

def create_department(db: Session, name: str, manager_id: int = None):
    db_dept = Department(name=name, manager_id=manager_id)
    db.add(db_dept)
    db.commit()
    db.refresh(db_dept)
    return db_dept