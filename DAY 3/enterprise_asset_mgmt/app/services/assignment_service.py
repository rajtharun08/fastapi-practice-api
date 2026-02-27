from sqlalchemy.orm import Session
from app.repositories import assignment_repo, asset_repo
from app.models.asset import AssetStatus

def assign_asset(db: Session, asset_id: int, user_id: int):
    asset = asset_repo.get_asset_by_id(db, asset_id)
    if not asset or asset.status != AssetStatus.AVAILABLE:
        return None
    assignment = assignment_repo.create_assignment(db, asset_id, user_id)
    asset_repo.update_asset_status(db, asset_id, AssetStatus.ASSIGNED)
    
    return assignment