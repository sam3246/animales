from fastapi import FastAPI

from models import models 
from database.conexion import Base, engine
from routers import animales, usuarios

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Animal API")

app.include_router(animales.router)
app.include_router(usuarios.router)