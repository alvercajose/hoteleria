from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.habitacion import Habitacion
from app.schemas.habitacion import HabitacionBase, HabitacionOut

router = APIRouter(prefix="/habitaciones", tags=["Habitaciones"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=HabitacionOut)
def crear_habitacion(habitacion: HabitacionBase, db: Session = Depends(get_db)):
    db_habitacion = Habitacion(**habitacion.dict())
    db.add(db_habitacion)
    db.commit()
    db.refresh(db_habitacion)
    return db_habitacion

@router.get("/", response_model=list[HabitacionOut])
def listar_habitaciones(db: Session = Depends(get_db)):
    return db.query(Habitacion).all()
