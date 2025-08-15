from pydantic import BaseModel
from datetime import date

class ReporteBase(BaseModel):
    tipo_reporte: str
    fecha: date
    contenido: str

class ReporteCreate(ReporteBase):
    pass

class ReporteOut(ReporteBase):
    id: int

    class Config:
        from_attributes = True
