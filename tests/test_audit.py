from fastapi.testclient import TestClient
from app.main import app
from app.core.audit import _AUDIT

client = TestClient(app)

def test_audit_endpoint_dev_mode_allows_without_token():
    # Clear audit log
    _AUDIT.clear()
    
    # Make a request that should be logged
    r = client.get("/v1/capabilities")
    assert r.status_code == 200
    
    # Check that audit event was logged
    r = client.get("/v1/audit/recent")
    assert r.status_code == 200
    assert "events" in r.json()