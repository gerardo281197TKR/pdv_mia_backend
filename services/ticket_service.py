from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.ticket import Ticket  # Asegúrate de que el modelo se llame correctamente
from schemas.ticket import TicketCreate, TicketUpdate  # Asegúrate de tener TicketUpdate si lo necesitas

def store_ticket(db: Session, ticket: TicketCreate):
    db_ticket = Ticket(**ticket.dict())
    print("aqui -------------")
    print("📨 Ticket dict:", ticket.dict())
    print("aqui -------------")
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def get_tickets(
    db: Session,
    client_id: int = None,
    status: str = None,
):
    query = db.query(Ticket)
    if client_id:
        query = query.filter(Ticket.clientId == client_id)
    if status:
        query = query.filter(Ticket.status == status)
    return query.all()

def get_ticket_by_id(db: Session, id: int):
    ticket = db.query(Ticket).filter(Ticket.id == id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

def update_ticket(db: Session, id: int, ticket_update: TicketUpdate):
    ticket = db.query(Ticket).filter(Ticket.id == id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    for key, value in ticket_update.dict(exclude_unset=True).items():
        setattr(ticket, key, value)

    db.commit()
    db.refresh(ticket)
    return ticket

def delete_ticket(db: Session, id: int):
    ticket = db.query(Ticket).filter(Ticket.id == id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    db.delete(ticket)
    db.commit()
    return {"message": "Ticket deleted successfully"}
