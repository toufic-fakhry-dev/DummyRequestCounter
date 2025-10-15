from fastapi.testclient import TestClient
import app.app as app_module  # imports FastAPI app from app/app.py

# simple in-memory fake Redis for unit tests
class FakeRedis:
    def __init__(self):
        self.store = {"hits": 0}
    def incr(self, key):
        self.store[key] = int(self.store.get(key, 0)) + 1
        return self.store[key]
    def get(self, key):
        return str(self.store.get(key, 0)).encode("utf-8")

# patch the module-level redis client used by the app
app_module.redis = FakeRedis()
client = TestClient(app_module.app)

def test_root_increments_and_returns_text():
    r1 = client.get("/")
    assert r1.status_code == 200
    assert "visited" in r1.text

    r2 = client.get("/")
    assert r2.status_code == 200
    assert "visited" in r2.text
    assert ("visited 2" in r2.text) or ("visited 2 times" in r2.text)
