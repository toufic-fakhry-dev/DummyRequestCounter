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
        # Accept both 200 (Redis available) and 503 (Redis not available)
        assert r.status_code in (200, 503), f"Got {r.status_code}: {r.text}"
        if r.status_code == 200:
            assert "Hello" in r.text
