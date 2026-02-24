from app.core.db import events_db

class EventRepository:
    def __init__(self):
        self._db = events_db
        if not self._db:
            self._db.append({"id": 1, "name": "Python Workshop", "location": "Chennai", "capacity": 100})
            self._db.append({"id": 2, "name": "Web Development", "location": "Bangalore", "capacity": 50})

    def get_all(self):
        return self._db

    def get_by_id(self, event_id: int):
        for event in self._db:
            if event["id"] == event_id:
                return event
        return None

    def create(self, event_data):
        event_dict = event_data.model_dump() if hasattr(event_data, "model_dump") else event_data.dict()
        event_dict["id"] = len(self._db) + 1
        self._db.append(event_dict)
        return event_dict

    def filter_by_location(self, location: str):
        return [e for e in self._db if e["location"].lower() == location.lower()]