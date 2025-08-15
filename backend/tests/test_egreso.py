import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_egreso():
    data = {
        "monto": 150.75,
        "fecha": "2025-07-09",
        "concepto": "Compra insumos"
    }
    response = client.post("/egresos/", json=data)
    assert response.status_code == 200
    json_resp = response.json()
    assert float(json_resp["monto"]) == 150.75
    assert json_resp["concepto"] == "Compra insumos"
    assert "id" in json_resp

def test_listar_egresos():
    response = client.get("/egresos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
