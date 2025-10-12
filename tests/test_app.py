import pytest
import sys
import os
from unittest.mock import Mock, patch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.app import app
from fastapi.testclient import TestClient


@pytest.fixture(autouse=True)
def mock_redis():
    with patch('app.app.redis') as mock_redis:
    
        mock_redis.incr.return_value = 1
        mock_redis.get.return_value = b'5'  
        yield mock_redis

client = TestClient(app)

def test_hello_route(mock_redis):
    """Test the main hello route with mocked Redis"""
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello" in response.text
    assert "visited" in response.text
    assert "times" in response.text
    

    mock_redis.incr.assert_called_once_with('hits')
    mock_redis.get.assert_called_once_with('hits')

def test_response_structure(mock_redis):
    """Test that response contains expected text"""
    response = client.get("/")
    assert response.status_code == 200
  
    assert "visited" in response.text.lower()
    assert "times" in response.text.lower()

def test_multiple_requests(mock_redis):
    """Test making multiple requests"""
    response1 = client.get("/")
    response2 = client.get("/")
    
    assert response1.status_code == 200
    assert response2.status_code == 200
    

    mock_redis.incr.reset_mock()
    mock_redis.get.reset_mock()
    
    
    client.get("/")
    client.get("/")
    

    assert mock_redis.incr.call_count == 2
    assert mock_redis.get.call_count == 2