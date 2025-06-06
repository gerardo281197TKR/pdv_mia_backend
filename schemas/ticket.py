from enum import Enum
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TicketStatus(str, Enum):
    pending = "pending"
    paid = "paid"
    canceled = "canceled"

class TypePayment(str, Enum):
    cash = "cash"
    transfer = "transfer"
    deposit = "deposit"

class TicketBase(BaseModel):
    clientId: int
    amount: Optional[float] = None
    status: Optional[TicketStatus] = TicketStatus.pending
    typePayment: Optional[str] = TypePayment.cash
    created_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None 

class TicketCreate(TicketBase):
    pass

class TicketUpdate(BaseModel):
    amount: Optional[float] = None
    typePayment: Optional[str] = None
    deleted_at: Optional[datetime] = None

class TicketOut(TicketBase):
    id: int

    class Config:
        orm_mode = True
