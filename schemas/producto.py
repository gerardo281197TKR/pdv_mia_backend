from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductoBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None 
    picture: Optional[str] = None
    created_at: Optional[datetime] = None
    deletd_at: Optional[datetime] = None 

class ProductoCreate(ProductoBase):
    pass

class ProductoOut(ProductoBase):
    id: int

    class Config:
        orm_mode = True

class ProductoUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    picture: Optional[str] = None
    stock: Optional[int] = None