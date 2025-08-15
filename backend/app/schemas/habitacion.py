from pydantic import BaseModel
from decimal import Decimal

class HabitacionBase(BaseModel):
    numero_habitacion: str
    tipo_habitacion: str
    precio: Decimal
    disponibilidad: bool = True

class HabitacionOut(HabitacionBase):
    id: int

    class Config:
        from_attributes = True
