import sys
import os
import pytest
from fastapi.testclient import TestClient

# Ensure app is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.app import app  # noqa: E402

client = TestClient(app)


def test_root_endpoint():
    """Test that the root endpoint returns the correct message."""
    response = client.get("/")
    assert response.status_code == 200
    assert "visited" in response.json()["message"]
    assert response.json()["message"].startswith("Hello!")


def test_root_endpoint_counter():
    """Test that the counter increments on each request."""
    response1 = client.get("/")
    response2 = client.get("/")
    msg1 = response1.json()["message"]
    msg2 = response2.json()["message"]

    # Ensure the second message count is greater than the first
    count1 = int(msg1.split("visited ")[1].split(" ")[0])
    count2 = int(msg2.split("visited ")[1].split(" ")[0])
    assert count2 == count1 + 1
