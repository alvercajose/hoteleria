import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_crear_cliente():
    data = {
        "id": 1,
        "nombre": "Juan Pérez",
        "telefono": "0987654321",
        "correo": "juanperez@example.com",
        "direccion": "Av. Siempre Viva 123"
    }
    response = client.post("/clientes/", json=data)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["nombre"] == "Juan Pérez"
    assert "id" in json_data

def test_listar_clientes():
    response = client.get("/clientes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
