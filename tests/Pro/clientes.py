from pydantic import BaseModel
from typing import List

# Simulamos una base de datos en memoria
db_clientes = []

# Modelo de Cliente
class Cliente(BaseModel):
    id: int
    nombre: str
    telefono: str
    correo: str
    direccion: str

# Función para crear un cliente
def crear_cliente(cliente: Cliente):
    db_clientes.append(cliente)
    return cliente

# Función para listar clientes
def listar_clientes() -> List[Cliente]:
    return db_clientes
