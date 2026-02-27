from typing import TypeVar, Generic, List
from pydantic import BaseModel

T = TypeVar("T")

class Page(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    size: int

def paginate(query, page: int, size: int):
    total = query.count()
    items = query.offset((page - 1) * size).limit(size).all()
    return Page(items=items, total=total, page=page, size=size)