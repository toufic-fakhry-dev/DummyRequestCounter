# tests/test_app.py
import re
from fastapi.testclient import TestClient
import fakeredis

import app.app as app_module
from app.app import app  # FastAPI instance

def _use_fake_redis():
    """
    Replace the module-level `redis` instance in app.app with a FakeRedis,
    so the endpoint doesn't connect to a real server.
    """
    fake = fakeredis.FakeRedis()
    app_module.redis = fake
    return fake

def test_root_200_and_contains_text():
    _use_fake_redis()
    client = TestClient(app)
    r = client.get("/")
    assert r.status_code == 200
    assert "visited" in r.text.lower()

def test_counter_increments_hits_key():
    fake = _use_fake_redis()
    client = TestClient(app)

    r1 = client.get("/")
    r2 = client.get("/")

    assert r1.status_code == 200 and r2.status_code == 200

    raw = fake.get("hits")
    assert raw is not None and int(raw) >= 2

    nums = [int(x) for x in re.findall(r"\d+", r2.text)]
    assert nums and nums[0] >= 2
