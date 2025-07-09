
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_obtener_reporte():
    response = client.get("/reportes/")
    assert response.status_code == 200

    json_resp = response.json()

    assert isinstance(json_resp, list)
    assert len(json_resp) > 0 


    for reporte in json_resp:
        assert isinstance(reporte, dict)
        assert "id" in reporte
        assert "tipo_reporte" in reporte
        assert "fecha" in reporte
        assert "contenido" in reporte