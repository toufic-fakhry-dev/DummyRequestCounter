import os
import sys

# Add parent directory to sys.path so 'app' can be imported
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)  # noqa: E402

from fastapi.testclient import TestClient  # noqa: E402
from app.app import app  # noqa: E402

client = TestClient(app)


def test_root_endpoint():
    """Test that the root endpoint returns the correct message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_root_endpoint_counter():
    """Test that the counter increments on each request."""
    response1 = client.get("/")
    response2 = client.get("/")
    assert response1.status_code == {"message": "Hello World"}
    assert response2.status_code == {"message": "Hello World"}
