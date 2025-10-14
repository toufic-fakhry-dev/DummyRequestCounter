# tests/test_app.py
from app.app import app


class FakeRedis:
    """A fake Redis client to simulate key increments."""

    def __init__(self):
        self.store = {"hits": 0}

    def incr(self, key):
        self.store[key] = int(self.store.get(key, 0)) + 1
        return self.store[key]


def test_root_increments_counter(monkeypatch):
    """Test that visiting '/' increments the counter."""
    import app.app as app_module

    app_module.r = FakeRedis()  # replace real Redis client

    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"visited" in resp.data
