from sqlalchemy.orm import Session
from models.producto import Producto
from schemas.producto import ProductoCreate

def crear_producto(db: Session, producto: ProductoCreate):
    db_producto = Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def obtener_productos(
        db: Session,
        nombre: str = None,
        precio_min: float = None,
        precio_max:float = None
    ):
    query = db.query(Producto)

    if nombre:
        query = query.filter(Producto.nombre.ilike(f"%{nombre}%"))
    
    if precio_min:
        query = query.filter(Producto.precio >= precio_min)
    
    if precio_max:
        query = query.filter(Producto.precio <= precio_max)

    return query.all()
