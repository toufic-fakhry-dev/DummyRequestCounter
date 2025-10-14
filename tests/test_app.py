import pytest
import asyncio
from httpx import AsyncClient
from app.app import app
import os

# Set test environment variables
os.environ["REDIS_HOST"] = "localhost"
os.environ["REDIS_PORT"] = "6379"
os.environ["REDIS_DB"] = "1"  # Use different DB for tests

@pytest.mark.asyncio
async def test_health_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

@pytest.mark.asyncio
async def test_root_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    data = response.json()
    # Should have either message (if Redis works) or error (if Redis unavailable)
    assert "message" in data or "error" in data
    
    # If Redis is unavailable, should still return hits: 0
    if "error" in data:
        assert "hits" in data
        assert data["hits"] == 0
    
    # If Redis works, should have message with visit count
    if "message" in data:
        assert "visited" in data["message"]
        assert "times" in data["message"]

@pytest.mark.asyncio
async def test_count_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/count")
    assert response.status_code == 200
    data = response.json()
    # Should have either count or error
    assert "count" in data
    # Count should be a number (0 if Redis unavailable)
    assert isinstance(data["count"], int)

@pytest.mark.asyncio
async def test_reset_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/reset")
    assert response.status_code == 200
    data = response.json()
    # Should have either message (success) or error (Redis unavailable)
    assert "message" in data or "error" in data

@pytest.mark.asyncio
async def test_counter_functionality():
    """Test that endpoints return consistent structure regardless of Redis availability"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Reset counter (should work even if Redis unavailable)
        reset_response = await ac.get("/reset")
        assert reset_response.status_code == 200
        
        # Get initial count
        count_response = await ac.get("/count")
        assert count_response.status_code == 200
        initial_count = count_response.json().get("count", 0)
        
        # Hit main endpoint
        root_response = await ac.get("/")
        assert root_response.status_code == 200
        
        # Check count after (may or may not increment depending on Redis)
        final_count_response = await ac.get("/count")
        assert final_count_response.status_code == 200
        final_count = final_count_response.json().get("count", 0)
        
        # Count should either stay same (no Redis) or increment (with Redis)
        assert final_count >= initial_count

@pytest.mark.asyncio
async def test_api_response_structure():
    """Test that all endpoints return valid JSON structure"""
    endpoints = ["/health", "/", "/count", "/reset"]
    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        for endpoint in endpoints:
            response = await ac.get(endpoint)
            assert response.status_code == 200
            
            # Should be valid JSON
            data = response.json()
            assert isinstance(data, dict)
            
            # Should have content-type header
            assert "application/json" in response.headers.get("content-type", "")

@pytest.mark.asyncio
async def test_redis_error_handling():
    """Test that app gracefully handles Redis connection issues"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # These should all work even without Redis
        health_response = await ac.get("/health")
        assert health_response.status_code == 200
        
        root_response = await ac.get("/")
        assert root_response.status_code == 200
        
        count_response = await ac.get("/count")
        assert count_response.status_code == 200
        
        reset_response = await ac.get("/reset")
        assert reset_response.status_code == 200