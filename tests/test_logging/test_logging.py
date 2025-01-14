from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_logging_get_logging() -> None:
    response = client.get("/logging/get_all")
    assert response.status_code == 200

def test_logging_get_next_entry() -> None:
    response = client.get("/logging/get_next_entry")
    assert response.status_code == 200