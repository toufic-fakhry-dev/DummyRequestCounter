# tests/test_app.py
from fastapi.testclient import TestClient
import pytest
import app.app as app_module  # import the module so we can patch its redis client

client = TestClient(app_module.app)


@pytest.fixture(autouse=True)
def fake_redis(monkeypatch):
    """
    Automatically replace the real Redis client in app.app with an in-memory fake
    so tests don't need a running Redis container.
    Works whether the app uses `r` (newer code) or `redis` (older code).
    """
    class FakeRedis:
        def __init__(self):
            self.store = {}

        def incr(self, key):
            self.store[key] = self.store.get(key, 0) + 1
            return self.store[key]

        # Return BYTES so older code that does .decode('utf-8') still works.
        def get(self, key):
            return str(self.store.get(key, 0)).encode("utf-8")

        def ping(self):
            return True

    fake = FakeRedis()

    # Figure out which name the app uses for its client and patch it.
    attr = "r" if hasattr(app_module, "r") else ("redis" if hasattr(app_module, "redis") else None)
    assert attr, "Could not find redis client variable ('r' or 'redis') in app.app"
    monkeypatch.setattr(app_module, attr, fake)

    return fake


def test_health_endpoint():
    # Should be 200 now that ping() is faked
    resp = client.get("/health")
    assert resp.status_code == 200


def test_root_endpoint():
    resp = client.get("/")
    assert resp.status_code == 200
    assert "Hello" in resp.text
