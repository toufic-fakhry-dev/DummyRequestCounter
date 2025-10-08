import os
import sys

# Add the project root to sys.path so we can import the app package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app.app import app


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to DummyRequestCounter!"}


def test_request_count():
    # First request
    response1 = client.get("/count")
    assert response1.status_code == 200
    data1 = response1.json()

    # Second request
    response2 = client.get("/count")
    data2 = response2.json()

    assert data2["count"] == data1["count"] + 1
