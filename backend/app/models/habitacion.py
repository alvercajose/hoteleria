from sqlalchemy import Column, Integer, String, Boolean, DECIMAL
from app.database import Base

class Habitacion(Base):
    __tablename__ = "habitaciones"

    id = Column(Integer, primary_key=True, index=True)
    numero_habitacion = Column(String(50), unique=True, nullable=False)
    tipo_habitacion = Column(String(50), nullable=False)
    precio = Column(DECIMAL(10, 2), nullable=False)
    disponibilidad = Column(Boolean, default=True)