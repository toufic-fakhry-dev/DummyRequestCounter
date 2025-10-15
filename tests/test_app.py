from fastapi.testclient import TestClient
from app.app import app   # <── dossier.app-fichier.app-variable

client = TestClient(app)

def test_homepage_returns_200():
    """
    Vérifie que la route '/' renvoie bien un code 200 et contient le message attendu.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello!" in response.text