from fastapi import FastAPI

from app import models 
from app.database.conexion import Base, engine
from app.routers import animales, usuarios

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Animal API")

app.include_router(animales.router)
app.include_router(usuarios.router)