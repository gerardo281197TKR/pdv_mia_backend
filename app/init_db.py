from app.database import Base, engine
from models import producto

def init_db():
    Base.metadata.create_all(bind=engine)
