from pydantic import BaseModel
from datetime import date
from decimal import Decimal

class EgresoBase(BaseModel):
    monto: Decimal
    fecha: date
    concepto: str

class EgresoCreate(EgresoBase):
    pass

class EgresoOut(EgresoBase):
    id: int

    class Config:
        from_attributes = True
