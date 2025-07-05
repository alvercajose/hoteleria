from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.controllers import cliente_controller, habitacion_controller
from app.database import Base, engine
from app.models import ingreso
from app.models import reporte  

app = FastAPI()

# Crea las tablas automáticamente
Base.metadata.create_all(bind=engine)

# Incluir rutas
app.include_router(cliente_controller.router)
app.include_router(habitacion_controller.router)

#-----
@app.get("/")
def root():
    return RedirectResponse(url="/docs")
from app.controllers import ingreso,egreso,reporte
app.include_router(ingreso.router)
app.include_router(egreso.router)
app.include_router(reporte.router)