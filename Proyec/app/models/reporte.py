
from sqlalchemy import Column, Integer, String, Date, Text
from app.database import Base

class Reporte(Base):
    __tablename__ = "reportes"

    id = Column(Integer, primary_key=True, index=True)
    tipo_reporte = Column(String(50))
    fecha = Column(Date)
    contenido = Column(Text)