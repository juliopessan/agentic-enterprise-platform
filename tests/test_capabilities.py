from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_capabilities_dev_mode_allows_without_token():
    r = client.get("/v1/capabilities")
    assert r.status_code == 200
    assert "capabilities" in r.json()