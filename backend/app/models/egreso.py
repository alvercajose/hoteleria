from sqlalchemy import Column, Integer, String, Date, DECIMAL
from app.database import Base

class Egreso(Base):
    __tablename__ = "egresos"

    id = Column(Integer, primary_key=True, index=True)
    monto = Column(DECIMAL(10, 2))
    fecha = Column(Date)
    concepto = Column(String(100))
