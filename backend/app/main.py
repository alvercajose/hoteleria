
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import cliente_controller, habitacion_controller
from app.database import Base, engine
from app.models import ingreso
from app.models import reporte  

app = FastAPI()

# Crea las tablas automáticamente
Base.metadata.create_all(bind=engine)

#NUEVO

# Permitir peticiones desde el frontend en desarrollo
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
