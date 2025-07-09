from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    telefono = Column(String(15))
    correo = Column(String(100), unique=True)
    direccion = Column(Text)
