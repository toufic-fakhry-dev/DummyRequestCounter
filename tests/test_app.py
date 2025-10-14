# tests/test_app.py
from fastapi.testclient import TestClient


def test_health_endpoint():
    from app.app import app
    client = TestClient(app)
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json().get("status") in {"ok", "degraded"}


def test_root_endpoint_tolerates_no_redis():
    from app.app import app
    client = TestClient(app)
    r = client.get("/")
    assert r.status_code in (200, 503)
    if r.status_code == 200:
        assert "Hello" in r.text
