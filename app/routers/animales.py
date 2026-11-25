from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.conexion import get_db
from app.models.animal import Animal
from app.schemas.animal import AnimalCreate, AnimalResponse

router = APIRouter(prefix="/animales", tags=["Animales"])


@router.get("", response_model=list[AnimalResponse])
def get_animales(db: Session = Depends(get_db)):
    return db.query(Animal).all()


# Va antes de "/{animal_id}" para que quede claro que es una ruta fija.
@router.get("/especie/{especie}", response_model=list[AnimalResponse])
def filtrar_animales_especie(especie: str, db: Session = Depends(get_db)):
    return db.query(Animal).filter(Animal.especie == especie).all()


@router.get("/{animal_id}", response_model=AnimalResponse)
def get_animal(animal_id: int, db: Session = Depends(get_db)):
    animal = db.query(Animal).filter(Animal.id == animal_id).first()
    if animal is None:
        raise HTTPException(status_code=404, detail="Animal no encontrado")
    return animal


@router.post("", response_model=AnimalResponse, status_code=201)
def create_animal(data: AnimalCreate, db: Session = Depends(get_db)):
    existing = db.query(Animal).filter(Animal.name == data.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Este animal ya existe")

    animal = Animal(**data.model_dump())
    db.add(animal)
    db.commit()
    db.refresh(animal)
    return animal


@router.put("/{animal_id}", response_model=AnimalResponse)
def update_animal(animal_id: int, data: AnimalCreate, db: Session = Depends(get_db)):
    animal = db.query(Animal).filter(Animal.id == animal_id).first()
    if animal is None:
        raise HTTPException(status_code=404, detail="Animal no encontrado")

    for campo, valor in data.model_dump().items():
        setattr(animal, campo, valor)

    db.commit()
    db.refresh(animal)
    return animal


@router.delete("/{animal_id}")
def delete_animal(animal_id: int, db: Session = Depends(get_db)):
    animal = db.query(Animal).filter(Animal.id == animal_id).first()
    if animal is None:
        raise HTTPException(status_code=404, detail="Animal no encontrado")

    db.delete(animal)
    db.commit()
    return {"message": "Animal eliminado correctamente"}
