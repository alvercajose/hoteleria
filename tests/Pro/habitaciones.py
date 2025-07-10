from pydantic import BaseModel
from typing import List

# Simulamos una base de datos en memoria
db_habitaciones = []

# Modelo de Habitacion
class Habitacion(BaseModel):
    id: int
    numero_habitacion: str
    tipo_habitacion: str
    precio: float
    disponibilidad: bool

# Función para crear una habitacion
def crear_habitacion(habitacion: Habitacion):
    db_habitaciones.append(habitacion)
    return habitacion

# Función para listar habitaciones
def listar_habitaciones() -> List[Habitacion]:
    return db_habitaciones
