import sys
import os
from unittest.mock import patch, MagicMock

# Mock the CrewAI imports to avoid requiring API keys during testing
sys.modules['crewai'] = MagicMock()
sys.modules['app.agents.hr.talent_ops'] = MagicMock()
sys.modules['app.agents.hr.people_lifecycle'] = MagicMock()
sys.modules['app.agents.hr.compliance'] = MagicMock()
sys.modules['app.agents.finance.accounts_payable'] = MagicMock()
sys.modules['app.agents.finance.accounts_receivable'] = MagicMock()
sys.modules['app.agents.finance.risk'] = MagicMock()
sys.modules['app.agents.legal.contract_review'] = MagicMock()
sys.modules['app.agents.legal.compliance_monitoring'] = MagicMock()
sys.modules['app.agents.legal.litigation_support'] = MagicMock()
sys.modules['app.agents.marketing.campaign_management'] = MagicMock()
sys.modules['app.agents.marketing.content_creation'] = MagicMock()
sys.modules['app.agents.marketing.analytics_reporting'] = MagicMock()

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_legal_module_in_capabilities():
    r = client.get("/v1/capabilities")
    assert r.status_code == 200
    capabilities = r.json()["capabilities"]
    
    # Check that legal module crews are listed
    legal_crews = [c for c in capabilities if c["module"] == "legal"]
    assert len(legal_crews) == 3
    legal_crew_names = [c["crew"] for c in legal_crews]
    assert "ContractReviewCrew" in legal_crew_names
    assert "ComplianceMonitoringCrew" in legal_crew_names
    assert "LitigationSupportCrew" in legal_crew_names

def test_marketing_module_in_capabilities():
    r = client.get("/v1/capabilities")
    assert r.status_code == 200
    capabilities = r.json()["capabilities"]
    
    # Check that marketing module crews are listed
    marketing_crews = [c for c in capabilities if c["module"] == "marketing"]
    assert len(marketing_crews) == 3
    marketing_crew_names = [c["crew"] for c in marketing_crews]
    assert "CampaignManagementCrew" in marketing_crew_names
    assert "ContentCreationCrew" in marketing_crew_names
    assert "AnalyticsReportingCrew" in marketing_crew_names

def test_legal_crew_execution_blocked_by_approval():
    payload = {
        "module": "legal",
        "crew": "ContractReviewCrew",
        "task": "review_contract",
        "payload": {"contract_id": "CT-2025-001", "amount": 75000},
        "autonomy_level": "L2",
        "approval": {
            "required": True,
            "threshold": 50000,
            "amount_field": "amount",
            "approved": False
        },
        "correlation_id": "legal-test-001"
    }
    
    r = client.post("/v1/agents/execute", json=payload)
    assert r.status_code == 200
    
    # Should return PENDING_APPROVAL status
    response_data = r.json()
    assert response_data["result"]["status"] == "PENDING_APPROVAL"
    assert "Approval required before execution" in response_data["result"]["message"]

def test_marketing_crew_execution_blocked_by_approval():
    payload = {
        "module": "marketing",
        "crew": "CampaignManagementCrew",
        "task": "launch_campaign",
        "payload": {"campaign_name": "Q1 Product Launch", "budget": 150000},
        "autonomy_level": "L2",
        "approval": {
            "required": True,
            "threshold": 100000,
            "amount_field": "budget",
            "approved": False
        },
        "correlation_id": "marketing-test-001"
    }
    
    r = client.post("/v1/agents/execute", json=payload)
    assert r.status_code == 200
    
    # Should return PENDING_APPROVAL status
    response_data = r.json()
    assert response_data["result"]["status"] == "PENDING_APPROVAL"
    assert "Approval required before execution" in response_data["result"]["message"]