from sqlalchemy import Column, Integer, Float, DateTime, Enum
from datetime import datetime
from app.database import Base
from enum import Enum as PyEnum 

class TicketStatus(PyEnum):
    PENDING = "pending"
    PAID = "paid"
    CANCELED = "canceled"

class TypePayment(PyEnum):
    CASH = "cash"
    TRANSFER = "transfer"
    DEPOSIT = "deposit"

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    clientId = Column(Integer, index=True)
    amount = Column(Float)
    typePayment = Column(Enum(TypePayment), default=TypePayment.CASH)
    status = Column(Enum(TicketStatus), default=TicketStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True, default=None)
