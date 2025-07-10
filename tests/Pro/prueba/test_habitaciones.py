import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_crear_habitacion():
    data = {
        "id": 1,
        "numero_habitacion": "A101",
        "tipo_habitacion": "Doble",
        "precio": 80.50,
        "disponibilidad": True
    }
    response = client.post("/habitaciones/", json=data)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["numero_habitacion"] == "A101"
    assert "id" in json_data

def test_listar_habitaciones():
    response = client.get("/habitaciones/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
