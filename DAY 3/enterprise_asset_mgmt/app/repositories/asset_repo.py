from sqlalchemy.orm import Session
from app.models.asset import Asset, AssetStatus
from datetime import datetime

def get_asset_by_tag(db: Session, asset_tag: str):
    return db.query(Asset).filter(Asset.asset_tag == asset_tag).first()

def get_assets_paginated(db: Session, skip: int, limit: int, status: str = None):
    query = db.query(Asset)
    if status:
        query = query.filter(Asset.status == status)
    return query.offset(skip).limit(limit).all()

def create_asset(db: Session, asset_data: dict):
    p_date = asset_data["purchase_date"]
    if isinstance(p_date, str):
        p_date = datetime.strptime(p_date, "%Y-%m-%d").date()
    asset_data["purchase_date"] = p_date
    db_asset = Asset(**asset_data)
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

def update_asset_status(db: Session, asset_id: int, status: AssetStatus):
    asset = db.query(Asset).filter(Asset.id == asset_id).first()
    if asset:
        asset.status = status
        db.commit()
    return asset