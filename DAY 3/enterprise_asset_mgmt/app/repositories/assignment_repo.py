from sqlalchemy.orm import Session
from app.models.asset_assignment import AssetAssignment
from datetime import datetime

def create_assignment(db: Session, asset_id: int, user_id: int):
    db_assignment = AssetAssignment(
        asset_id=asset_id,
        user_id=user_id,
        assigned_date=datetime.utcnow()
    )
    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)
    return db_assignment

def get_active_assignment(db: Session, asset_id: int):
    return db.query(AssetAssignment).filter(
        AssetAssignment.asset_id == asset_id,
        AssetAssignment.returned_date == None
    ).first()

def close_assignment(db: Session, assignment_id: int, condition: str):
    assignment = db.query(AssetAssignment).filter(AssetAssignment.id == assignment_id).first()
    if assignment:
        assignment.returned_date = datetime.utcnow()
        assignment.condition_on_return = condition
        db.commit()
    return assignment