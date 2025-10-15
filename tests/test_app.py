import sys
import os
from fastapi.testclient import TestClient

# Ajouter le dossier racine au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.app import app  # ✅ correction ici

client = TestClient(app)

def test_homepage_returns_200():
    """
    Vérifie que la route '/' renvoie bien un code 200 et contient le message attendu.
    """
    response = client.get("/")  # nosec B101
    assert response.status_code == 200  # nosec B101
    assert "Hello!" in response.text  # nosec B101