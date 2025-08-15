from pydantic import BaseModel, ConfigDict
from datetime import date
from decimal import Decimal

class IngresoBase(BaseModel):
    monto: Decimal
    fecha: date
    concepto: str

class IngresoCreate(IngresoBase):
    pass

class IngresoOut(IngresoBase):
    id: int
    class Config:
        from_attributes = True  
