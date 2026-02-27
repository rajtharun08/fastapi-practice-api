from sqlalchemy.orm import Session
from app.repositories import asset_repo, assignment_repo
from app.models.asset import AssetStatus

def create_new_asset(db: Session, asset_data: dict):
    return asset_repo.create_asset(db, asset_data)

def process_asset_return(db: Session, assignment_id: int, condition: str):
    # Scenario 3: Asset Return [cite: 164]
    assignment = assignment_repo.close_assignment(db, assignment_id, condition)
    if assignment:
        # Rule: On return -> status changes to AVAILABLE [cite: 130]
        asset_repo.update_asset_status(db, assignment.asset_id, AssetStatus.AVAILABLE)
    return assignment