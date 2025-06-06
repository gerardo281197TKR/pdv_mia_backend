from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from schemas.ticket import TicketCreate, TicketOut, TicketUpdate
from services.ticket_service import (
    store_ticket, get_tickets, get_ticket_by_id, update_ticket, delete_ticket
)
from app.database import SessionLocal

router = APIRouter(prefix="/tickets", tags=["Tickets"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TicketOut)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    return store_ticket(db, ticket)

@router.get("/", response_model=list[TicketOut])
def list_tickets(
    client_id: int | None = Query(None),
    status: str | None = Query(None),
    db: Session = Depends(get_db)
):
    return get_tickets(db, client_id, status)

@router.get("/{id}", response_model=TicketOut)
def get_ticket(id: int, db: Session = Depends(get_db)):
    return get_ticket_by_id(db, id)

@router.put("/update/{id}", response_model=TicketOut)
def update_ticket_route(
    id: int,
    ticket_update: TicketUpdate,
    db: Session = Depends(get_db)
):
    return update_ticket(db, id, ticket_update)

@router.delete("/delete/{id}")
def delete_ticket_route(id: int, db: Session = Depends(get_db)):
    return delete_ticket(db, id)
