from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    nombre: str = Field(min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserUpdate(BaseModel):
    # Todos opcionales: solo se actualiza lo que se envíe.
    nombre: Optional[str] = Field(default=None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(default=None, min_length=8, max_length=128)
    activo: Optional[bool] = None


class UserResponse(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    activo: bool

    # La respuesta no incluye la contraseña.
    model_config = ConfigDict(from_attributes=True)
