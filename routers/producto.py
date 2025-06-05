from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from schemas.producto import ProductoCreate, ProductoOut
from services.producto_service import crear_producto, obtener_productos
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
    nombre: str | None = Query(None),
    precio_min : float | None = Query(None),
    precio_max : float | None = Query(None),
    db: Session = Depends(get_db)
):
    return obtener_productos(db, nombre, precio_min, precio_max)
