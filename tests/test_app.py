# tests/test_app.py
import sys
import os

# Ensure the app module can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient  #nosec E402
from app.app import app  #nosec E402

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_root_endpoint_counter():
    # Call the endpoint multiple times to check counter increments
    first = client.get("/").json()["message"]
    second = client.get("/").json()["message"]
    assert first != second
