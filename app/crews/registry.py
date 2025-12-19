from app.api.v1.schemas import AgentRequest, AgentResponse
from app.core.logging import get_logger
from app.core.audit import log_event
from app.crews.hr_crews import run_talent_ops, run_people_lifecycle, run_hr_compliance
from app.crews.finance_crews import run_accounts_payable, run_accounts_receivable, run_finance_risk
from app.crews.legal_crews import run_contract_review, run_compliance_monitoring, run_litigation_support
from app.crews.marketing_crews import run_campaign_management, run_content_creation, run_analytics_reporting

log = get_logger("registry")

REGISTRY = {
    "hr": {
        "TalentOpsCrew": run_talent_ops,
        "PeopleLifecycleCrew": run_people_lifecycle,
        "HRComplianceCrew": run_hr_compliance,
    },
    "finance": {
        "AccountsPayableCrew": run_accounts_payable,
        "AccountsReceivableCrew": run_accounts_receivable,
        "FinanceRiskCrew": run_finance_risk,
    },
    "legal": {
        "ContractReviewCrew": run_contract_review,
        "ComplianceMonitoringCrew": run_compliance_monitoring,
        "LitigationSupportCrew": run_litigation_support,
    },
    "marketing": {
        "CampaignManagementCrew": run_campaign_management,
        "ContentCreationCrew": run_content_creation,
        "AnalyticsReportingCrew": run_analytics_reporting,
    },
}

def list_capabilities():
    out = []
    for module, crews in REGISTRY.items():
        for crew_name in crews.keys():
            out.append({"module": module, "crew": crew_name})
    return out

def _approval_required(request: AgentRequest) -> bool:
    if not request.approval or not request.approval.required:
        return False
    amount_field = request.approval.amount_field or "amount"
    amount = request.payload.get(amount_field)
    if amount is None:
        return True
    try:
        amount_val = float(amount)
    except Exception:
        return True
    return amount_val > float(request.approval.threshold or 0.0)

def run_request(request: AgentRequest, ctx: dict | None = None) -> AgentResponse:
    module = request.module
    crew_name = request.crew
    if module not in REGISTRY:
        raise KeyError(f"Unknown module: {module}")
    if crew_name not in REGISTRY[module]:
        raise KeyError(f"Unknown crew for module {module}: {crew_name}")

    # Autonomy guardrails (MVP)
    requires_approval = _approval_required(request)
    if requires_approval and not (request.approval and request.approval.approved):
        meta = {
            "autonomy_level": request.autonomy_level,
            "requires_approval": True,
            "approval": request.approval.model_dump() if request.approval else None
        }
        log_event(
            correlation_id=request.correlation_id,
            module=module,
            crew=crew_name,
            task=request.task,
            status="blocked_requires_approval",
            meta={"ctx": ctx or {}, **meta}
        )
        return AgentResponse(
            correlation_id=request.correlation_id,
            module=module,
            crew=crew_name,
            task=request.task,
            result={"status": "PENDING_APPROVAL", "message": "Approval required before execution."},
            meta=meta
        )

    runner = REGISTRY[module][crew_name]
    log.info(f"Executing module={module} crew={crew_name} task={request.task} correlation_id={request.correlation_id}")
    log_event(
        correlation_id=request.correlation_id,
        module=module,
        crew=crew_name,
        task=request.task,
        status="started",
        meta={"ctx": ctx or {}, "autonomy_level": request.autonomy_level}
    )

    result = runner(request.task, request.payload)

    log_event(
        correlation_id=request.correlation_id,
        module=module,
        crew=crew_name,
        task=request.task,
        status="completed",
        meta={"ctx": ctx or {}, "autonomy_level": request.autonomy_level}
    )

    return AgentResponse(
        correlation_id=request.correlation_id,
        module=module,
        crew=crew_name,
        task=request.task,
        result=result,
        meta={"autonomy_level": request.autonomy_level, "requires_approval": False}
    )
