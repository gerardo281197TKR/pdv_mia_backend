from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    stock = Column(Integer)
    picture = Column(String, nullable=True)
