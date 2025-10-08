from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.app import app  # your FastAPI app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
