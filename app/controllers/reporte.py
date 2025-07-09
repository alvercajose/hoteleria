from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.models.reporte import Reporte
from app.schemas.reporte import ReporteCreate, ReporteOut
from app.database import SessionLocal


def crear_reporte(db: Session, reporte: ReporteCreate):
    nuevo = Reporte(**reporte.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def listar_reportes(db: Session):
    return db.query(Reporte).all()

#------------
#routers
router = APIRouter(prefix="/reportes", tags=["Reportes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ReporteOut)
def crear(reporte: ReporteCreate, db: Session = Depends(get_db)):
    return crear_reporte(db, reporte)

@router.get("/", response_model=list[ReporteOut])
def listar(db: Session = Depends(get_db)):
    return listar_reportes(db)
