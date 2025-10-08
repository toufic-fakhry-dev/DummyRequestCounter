import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
from app.app import app

# Mock Redis for testing
@pytest.fixture(autouse=True)
def mock_redis():
    with patch('app.app.redis') as mock_redis:
        # Set up mock behavior - return bytes like real Redis
        mock_redis.incr.return_value = 1
        mock_redis.get.return_value = b"1"  # Return bytes instead of string
        yield mock_redis

client = TestClient(app)

def test_hello_endpoint():
    """Test the hello endpoint returns successful response"""
    response = client.get("/")
    assert response.status_code == 200
    assert "visited" in response.text.lower()
    assert "1" in response.text

def test_hello_endpoint_increments_counter():
    """Test that counter increments on each call"""
    # Mock different return values for each call
    with patch('app.app.redis') as mock_redis:
        # First call
        mock_redis.incr.return_value = 1
        mock_redis.get.return_value = b"1"
        response1 = client.get("/")

        # Second call
        mock_redis.incr.return_value = 2
        mock_redis.get.return_value = b"2"
        response2 = client.get("/")

    assert response1.status_code == 200
    assert response2.status_code == 200
    assert "1" in response1.text
    assert "2" in response2.text

def test_health_endpoint():
    """Test health endpoint if it exists"""
    pass