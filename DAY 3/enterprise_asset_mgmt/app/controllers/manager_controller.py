from sqlalchemy.orm import Session
from app.models.asset_assignment import AssetAssignment
from app.models.user import User

def get_team_assets(db: Session, manager_id: int):
    manager = db.query(User).filter(User.id == manager_id).first()
    return db.query(AssetAssignment).join(User).filter(
        User.department_id == manager.department_id
    ).all()