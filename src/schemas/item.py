from datetime import datetime
from pydantic import BaseModel, ConfigDict

class ItemBase(BaseModel):
    name: str
    description: str

class Item(ItemBase):
    pass

class ItemOrm(ItemBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime
    updated_at: datetime