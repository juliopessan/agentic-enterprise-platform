from fastapi.testclient import TestClient
from app.main import app
from app.core.audit import _AUDIT

client = TestClient(app)

def test_approval_workflow_blocks_execution():
    # Clear audit log
    _AUDIT.clear()
    
    # Make a request with approval required but not approved
    payload = {
        "module": "finance",
        "crew": "AccountsPayableCrew",
        "task": "validate_invoice",
        "payload": {"invoice_id": "INV-8842", "amount": 6500},
        "autonomy_level": "L2",
        "approval": {
            "required": True,
            "threshold": 5000,
            "amount_field": "amount",
            "approved": False
        },
        "correlation_id": "test-001"
    }
    
    r = client.post("/v1/agents/execute", json=payload)
    assert r.status_code == 200
    
    # Should return PENDING_APPROVAL status
    response_data = r.json()
    assert response_data["result"]["status"] == "PENDING_APPROVAL"
    assert "Approval required before execution" in response_data["result"]["message"]
    
    # Check that audit event was logged
    r = client.get("/v1/audit/recent")
    assert r.status_code == 200
    events = r.json()["events"]
    assert len(events) > 0
    assert events[0]["status"] == "blocked_requires_approval"