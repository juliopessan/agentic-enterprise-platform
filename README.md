# Agentic Enterprise Platform (AEP)

Plug-and-play AI Agents for enterprise operations using **CrewAI + FastAPI**.

## Modules
- HR: TalentOpsCrew, PeopleLifecycleCrew, HRComplianceCrew
- Finance: AccountsPayableCrew, AccountsReceivableCrew, FinanceRiskCrew
- Legal: ContractReviewCrew, ComplianceMonitoringCrew, LitigationSupportCrew
- Marketing: CampaignManagementCrew, ContentCreationCrew, AnalyticsReportingCrew

## Auth (MVP)
- Set `API_TOKEN` and call the API with `Authorization: Bearer <API_TOKEN>`.
- If `ENVIRONMENT=dev`, missing token is allowed for local dev.

## Run locally (Docker)
```bash
cp .env.example .env
docker build -t aep .
docker run --env-file .env -p 8000:8000 aep
```

## Run locally (Python)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY=...
export API_TOKEN=change_me
uvicorn app.main:app --reload
```

## API
### Execute an agent crew
`POST /v1/agents/execute`

Example payload (basic):
```json
{
  "module": "finance",
  "crew": "AccountsPayableCrew",
  "task": "validate_invoice",
  "payload": {"invoice_id": "INV-8842"},
  "autonomy_level": "L1",
  "correlation_id": "demo-001"
}
```

Example payload (with approval control):
```json
{
  "module": "finance",
  "crew": "AccountsPayableCrew",
  "task": "validate_invoice",
  "payload": {"invoice_id": "INV-8842", "amount": 6500},
  "autonomy_level": "L2",
  "approval": {
    "required": true,
    "threshold": 5000,
    "amount_field": "amount",
    "approved": false
  },
  "correlation_id": "demo-001"
}
```

Example payload (legal module):
```json
{
  "module": "legal",
  "crew": "ContractReviewCrew",
  "task": "review_contract",
  "payload": {"contract_id": "CT-2025-001", "amount": 75000},
  "autonomy_level": "L2",
  "approval": {
    "required": true,
    "threshold": 50000,
    "amount_field": "amount",
    "approved": false
  },
  "correlation_id": "legal-demo-001"
}
```

Example payload (marketing module):
```json
{
  "module": "marketing",
  "crew": "CampaignManagementCrew",
  "task": "launch_campaign",
  "payload": {"campaign_name": "Q1 Product Launch", "budget": 150000},
  "autonomy_level": "L2",
  "approval": {
    "required": true,
    "threshold": 100000,
    "amount_field": "budget",
    "approved": false
  },
  "correlation_id": "marketing-demo-001"
}
```

## New Endpoints
- `GET /v1/capabilities` - List all available modules and crews
- `GET /v1/audit/recent` - View recent audit events

## Next planned steps
- Auth/RBAC (Azure AD)
- Human-in-the-loop thresholds
- Observability (OpenTelemetry)
- Real tools for ERP/ATS/OCR
