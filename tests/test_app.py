import pytest
from app import app as flask_app
import app.app as app_module


class FakeRedis:
    def __init__(self):
        self.store = {"hits": "0"}

    def incr(self, key):
        val = int(self.store.get(key, "0")) + 1
        self.store[key] = str(val)
        return val

    def get(self, key):
        return self.store.get(key, "0")


@pytest.fixture(autouse=True)
def patch_redis(monkeypatch):
    fake = FakeRedis()
    # patch the redis instance inside app.app module
    monkeypatch.setattr(app_module, "redis", fake)
    return fake


def test_root_increments_and_returns(patch_redis):
    flask_app.testing = True
    client = flask_app.test_client()

    resp1 = client.get("/")
    assert resp1.status_code == 200
    assert (
        "Hello! This page has been visited 1 times."
        in resp1.get_data(as_text=True)
    )

    resp2 = client.get("/")
    assert (
        "Hello! This page has been visited 2 times."
        in resp2.get_data(as_text=True)
    )
