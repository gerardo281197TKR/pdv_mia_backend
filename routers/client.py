from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlalchemy.orm import Session
from app.database import SessionLocal
from schemas.client import ClientCreate, ClientUpdate, ClientOut
from services.client_service import store_cliente, get_clients, findOne, delete, update

router = APIRouter(prefix="/clients", tags=["Clientes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[ClientOut])
def listar(
        name: str | None = Query(None),
        phone: str | None = Query(None),
        db: Session = Depends(get_db)
    ):
    return get_clients(db, name, phone)

@router.post('/', response_model=ClientOut)
def store(
    client: ClientCreate, 
    db: Session = Depends(get_db)     
):
    return store_cliente(db, client)

@router.get('/{id}', response_model=ClientOut)
def find_one(id: int, db: Session = Depends(get_db)):
    return findOne(db, id)

@router.post('/update/{id}', response_model=ClientOut)
def updateF(id: int, client_update: ClientUpdate, db: Session = Depends(get_db)):
    return update(db, id, client_update)

@router.delete('/delete/{id}')
def destroy(id: int, db: Session = Depends(get_db)):
    return delete(db, id)