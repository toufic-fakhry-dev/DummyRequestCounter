# tests/test_integration.py
import importlib
import pytest
from fastapi.testclient import TestClient

pytestmark = pytest.mark.integration

def test_root_with_redis(monkeypatch):

    monkeypatch.setenv("REDIS_HOST", "127.0.0.1")
    monkeypatch.setenv("REDIS_PORT", "6379")

    import app.app as app_module
    importlib.reload(app_module)
    
    with TestClient(app_module.app) as client:
        r = client.get("/")
        assert r.status_code == 200
        assert "Hello" in r.text
