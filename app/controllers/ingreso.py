
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.ingreso import Ingreso
from app.schemas.ingreso import IngresoCreate, IngresoOut
from app.database import SessionLocal

router = APIRouter(prefix="/ingresos", tags=["Ingresos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def crear_ingreso(db: Session, ingreso: IngresoCreate):
    nuevo = Ingreso(**ingreso.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def listar_ingresos(db: Session):
    return db.query(Ingreso).all()

@router.post("/", response_model=IngresoOut)
def crear(ingreso: IngresoCreate, db: Session = Depends(get_db)):
    return crear_ingreso(db, ingreso)

@router.get("/", response_model=list[IngresoOut])
def listar(db: Session = Depends(get_db)):
    return listar_ingresos(db)

