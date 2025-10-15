from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_app_request_counting():
    _status_code = 200
    _content = "Hello! This page has been visited"
    response = client.get("/")

    status_code = response.status_code
    content = response.text

    assert status_code == _status_code
    assert _content in content
