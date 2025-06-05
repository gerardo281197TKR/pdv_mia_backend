from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.producto import Producto
from schemas.producto import ProductoCreate, ProductoUpdate

def crear_producto(db: Session, producto: ProductoCreate):
    db_producto = Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def obtener_productos(
        db: Session,
        name: str = None,
        price_min: float = None,
        price_max:float = None
    ):
    query = db.query(Producto)

    if name:
        query = query.filter(Producto.name.ilike(f"%{name}%"))
    
    if price_min:
        query = query.filter(Producto.price >= price_min)
    
    if price_max:
        query = query.filter(Producto.price <= price_max)

    return query.all()

def findOne(db:Session, id: int):
    result = db.query(Producto).filter(Producto.id == id).first()
    return result

def update(db: Session, id: int, producto_update: ProductoUpdate):
    producto = db.query(Producto).filter(Producto.id == id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    # Actualizar sólo los campos que vienen en el request (no None)
    update_data = producto_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(producto, key, value)

    db.commit()
    db.refresh(producto)
    return producto

def delete(db: Session, id: int):
    product = db.query(Producto).filter(Producto.id == id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    db.delete(product)
    db.commit();
    return {"message": "Producto eliminado correctamente", "id": id}
