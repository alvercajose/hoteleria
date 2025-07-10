from fastapi import FastAPI
from clientes import Cliente, crear_cliente, listar_clientes
from habitaciones import Habitacion, crear_habitacion, listar_habitaciones

app = FastAPI()

@app.post("/clientes/")
def post_cliente(cliente: Cliente):
    return crear_cliente(cliente)

@app.get("/clientes/")
def get_clientes():
    return listar_clientes()

@app.post("/habitaciones/")
def post_habitacion(habitacion: Habitacion):
    return crear_habitacion(habitacion)

@app.get("/habitaciones/")
def get_habitaciones():
    return listar_habitaciones()

