# tests/test_app.py
from fastapi.testclient import TestClient
from app.app import app  # make sure this matches your FastAPI app location

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello" in response.json()["message"]
