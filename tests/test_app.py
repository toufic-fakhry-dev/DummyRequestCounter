import sys
import os
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch

# Ajouter le dossier racine au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.app import app

client = TestClient(app)

@pytest.fixture(autouse=True)
def mock_redis():
    """Mock des fonctions Redis pour éviter les connexions réelles pendant les tests."""
    with patch("app.app.redis") as mock_redis_client:
        mock_redis_client.incr.return_value = 1
        mock_redis_client.get.return_value = b"1"
        yield mock_redis_client


def test_homepage_returns_200():
    """
    Vérifie que la route '/' renvoie bien un code 200 et contient le message attendu.
    """
    response = client.get("/")  # nosec B101
    assert response.status_code == 200  # nosec B101
    assert "Hello!" in response.text  # nosec B101