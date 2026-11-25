from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.conexion import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserUpdate

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


def _email_en_uso(db: Session, email: str, excluir_id: int | None = None) -> bool:
    query = db.query(User).filter(User.email == email)
    if excluir_id is not None:
        query = query.filter(User.id != excluir_id)
    return query.first() is not None


@router.get("", response_model=list[UserResponse])
def get_usuarios(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.get("/{user_id}", response_model=UserResponse)
def get_usuario(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


@router.post("", response_model=UserResponse, status_code=201)
def create_usuario(data: UserCreate, db: Session = Depends(get_db)):
    if _email_en_uso(db, data.email):
        raise HTTPException(status_code=400, detail="Este email ya está registrado")

    user = User(
        nombre=data.nombre,
        email=data.email,
        password=data.password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.put("/{user_id}", response_model=UserResponse)
def update_usuario(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    cambios = data.model_dump(exclude_unset=True)

    if "email" in cambios and _email_en_uso(db, cambios["email"], excluir_id=user_id):
        raise HTTPException(status_code=400, detail="Este email ya está registrado")

    for campo, valor in cambios.items():
        setattr(user, campo, valor)

    db.commit()
    db.refresh(user)
    return user


@router.delete("/{user_id}")
def delete_usuario(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(user)
    db.commit()
    return {"message": "Usuario eliminado correctamente"}
