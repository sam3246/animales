from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AnimalCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    especie: str = Field(min_length=2, max_length=100)
    raza: Optional[str] = Field(default=None, max_length=100)
    fecha_nacimiento: Optional[str] = Field(default=None, max_length=10)
    propietario: Optional[str] = Field(default=None, max_length=100)


class AnimalResponse(BaseModel):
    id: int
    name: str
    especie: str
    raza: Optional[str] = None
    fecha_nacimiento: Optional[str] = None
    propietario: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
