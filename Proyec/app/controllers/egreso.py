#crud
from sqlalchemy.orm import Session
from app.models.egreso import Egreso
from fastapi import APIRouter, Depends
from app.schemas.egreso import EgresoCreate, EgresoOut
from app.database import SessionLocal

def crear_egreso(db: Session, egreso: EgresoCreate):
    nuevo = Egreso(**egreso.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def listar_egresos(db: Session):
    return db.query(Egreso).all()


#routers

router = APIRouter(prefix="/egresos", tags=["Egresos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EgresoOut)
def crear(egreso: EgresoCreate, db: Session = Depends(get_db)):
    return crear_egreso(db, egreso)

@router.get("/", response_model=list[EgresoOut])
def listar(db: Session = Depends(get_db)):
    return listar_egresos(db)
