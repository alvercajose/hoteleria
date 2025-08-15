from pydantic import BaseModel

class ClienteBase(BaseModel):
    nombre: str
    telefono: str
    correo: str
    direccion: str

class ClienteOut(ClienteBase):
    id: int

    class Config:
        from_attributes = True