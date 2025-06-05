from fastapi import FastAPI
from routers import producto
from app.init_db import init_db

app = FastAPI()

init_db()

app.include_router(producto.router)

@app.get("/")
def root():
    return {"mensaje": "PDV iniciado"}
