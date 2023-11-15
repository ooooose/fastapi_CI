from datetime import datetime
from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str

class Item(ItemBase):
    pass

class ItemOrm(ItemBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes=True