from sqlalchemy.orm import Session
from app.services import asset_service, request_service
from app.repositories import asset_repo

def add_asset(db: Session, asset_data: dict):
    return asset_service.create_new_asset(db, asset_data)

def approve_request(db: Session, request_id: int, asset_id: int, admin_id: int):
    return request_service.approve_request(db, request_id, asset_id, admin_id)

def return_asset(db: Session, assignment_id: int, condition: str):
    return asset_service.process_asset_return(db, assignment_id, condition)

def list_assets(db: Session, skip: int, limit: int, status: str = None):
    return asset_repo.get_assets_paginated(db, skip, limit, status)