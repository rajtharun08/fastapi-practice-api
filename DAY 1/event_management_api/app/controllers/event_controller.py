from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from app.schemas.event_schema import EventCreate, EventResponse
from app.dependencies.service_dependency import get_event_service

router = APIRouter(prefix="/events")

@router.post("/", response_model=EventResponse)
def create_event(event_data: EventCreate, service=Depends(get_event_service)):
    return service.create_event(event_data)

@router.get("/", response_model=List[EventResponse])
def list_events(location: Optional[str] = Query(None), service=Depends(get_event_service)):
    if location:
        return service.filter_events(location)
    return service.get_all_events()

@router.get("/{event_id}", response_model=EventResponse)
def get_event(event_id: int, service=Depends(get_event_service)):
    return service.get_event_by_id(event_id)