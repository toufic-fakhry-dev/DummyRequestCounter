# tests/test_app.py
from fastapi.testclient import TestClient
import app.main as main

client = TestClient(main.app)

def test_ping(monkeypatch):
    # Avoid needing a real Redis by mocking .ping()
    monkeypatch.setattr(main.r, "ping", lambda: True)
    resp = client.get("/ping")
    assert resp.status_code == 200
    assert resp.json() == {"pong": True}

def test_openapi_available():
    resp = client.get("/openapi.json")
    assert resp.status_code == 200
    assert "openapi" in resp.json()
