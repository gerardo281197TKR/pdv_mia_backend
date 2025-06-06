from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.client import Client
from schemas.client import ClientCreate, ClientUpdate

def store_cliente(db: Session, client:ClientCreate):
    db_client = Client(** client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_clients(
        db: Session,
        name: str = None,
        phone: str = None,
    ):
    query = db.query(Client)

    if name:
        query = query.filter(Client.name.ilike(f"%{name}%"))
    
    if phone:
        query = query.filter(Client.phone.ilike(f"%{phone}%"))
    
    return query.all()

def findOne(
        db: Session,
        id: int
    ):
    result = db.query(Client).filter(Client.id == id).first()
    return result

def update(
        db: Session,
        id: int,
        client_update: ClientUpdate    
    ):
    client = db.query(Client).filter(Client.id == id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    update_info = client_update.dict(exclude_unset=True)
    for key,value in update_info.items():
        setattr(client, key, value)
    
    db.commit()
    db.refresh(client)
    return client

def delete(db: Session, id: int):
    client = db.query(Client).filter(Client.id == id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    db.delete(client)
    db.commit()
    db.refresh(client)
    return {"message": "Client deleted successfully"}