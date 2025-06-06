from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ClientBase(BaseModel):
    name: str
    phone: Optional[str] = None
    direction: Optional[str] = None
    created_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None 

class ClientCreate(ClientBase):
    pass

class ClientOut(ClientBase):
    id: int

    class Config:
        orm_mode = True

class ClientUpdate(BaseModel):
    name: str
    phone: Optional[str] = None
    direction: Optional[str] = None