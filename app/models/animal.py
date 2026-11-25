from sqlalchemy import Column, Integer, String

from app.database.conexion import Base


class Animal(Base):
    __tablename__ = "animales"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    especie = Column(String(100), nullable=False)
    raza = Column(String(100), nullable=True)
    fecha_nacimiento = Column(String(10), nullable=True)
    propietario = Column(String(100), nullable=True)
