

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Hello World"}

def test_count_endpoint():
    r = client.get("/count")
    assert r.status_code == 200
    data = r.json()
    assert "counter" in data
    assert isinstance(data["counter"], int)

