from fastapi import FastAPI
from app.controllers import cliente_controller, habitacion_controller
from app.database import Base, engine

app = FastAPI()

# Crea las tablas automáticamente
Base.metadata.create_all(bind=engine)

# Incluir rutas
app.include_router(cliente_controller.router)
app.include_router(habitacion_controller.router)