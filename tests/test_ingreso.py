import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_ingreso():
    data = {
        "monto": 300.50,
        "fecha": "2025-07-09",
        "concepto": "Pago cliente"
    }
    response = client.post("/ingresos/", json=data)
    assert response.status_code == 200
    json_resp = response.json()
    assert float(json_resp["monto"]) == 300.50 # assert json_resp["monto"] == 300.50
    assert json_resp["concepto"] == "Pago cliente"
    assert "id" in json_resp

def test_listar_ingresos():
    response = client.get("/ingresos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
