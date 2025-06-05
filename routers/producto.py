from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlalchemy.orm import Session
from schemas.producto import ProductoCreate, ProductoOut, ProductoUpdate
from services.producto_service import crear_producto, obtener_productos, findOne, update, delete
from app.database import SessionLocal

router = APIRouter(prefix="/productos", tags=["Productos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProductoOut)
def crear(producto: ProductoCreate, db: Session = Depends(get_db)):
    return crear_producto(db, producto)

@router.get("/", response_model=list[ProductoOut])
def listar(
    name: str | None = Query(None),
    price_min : float | None = Query(None),
    price_max : float | None = Query(None),
    db: Session = Depends(get_db)
):
    return obtener_productos(db, name, price_min, price_max)

@router.get('/{id}', response_model=ProductoOut)
def findOneProduct(id:int, db: Session = Depends(get_db)):
    return findOne(db, id)

@router.post('/update/{id}', response_model=ProductoOut)
def updateProduct(
    id: int,
    producto_update: ProductoUpdate,
    db: Session = Depends(get_db)
):
    return update(db, id, producto_update)

@router.delete('/delete/{id}')
def deleteProduct(id: int, db: Session = Depends(get_db)):
    return delete(db, id)