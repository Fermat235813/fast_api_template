from fastapi.testclient import TestClient

from app.config.service import settings
from app.main import app

client = TestClient(app)

def test_get_config() -> None:
    response = client.get("/settings")
    assert response.status_code == 200

def test_set_dev() -> None:
    assert settings.ENVIRONMENT == "DEV"