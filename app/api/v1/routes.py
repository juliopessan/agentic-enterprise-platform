from fastapi import APIRouter, HTTPException, Header, Depends
from app.api.v1.schemas import AgentRequest, AgentResponse
from app.crews.registry import run_request, list_capabilities
from app.core.security import auth_context
from app.core.audit import recent as audit_recent

router = APIRouter()

def require_auth(authorization: str = Header(default=None)):
    return auth_context(authorization)

@router.get("/capabilities")
def capabilities(_: dict = Depends(require_auth)):
    return {"capabilities": list_capabilities()}

@router.get("/audit/recent")
def audit(limit: int = 50, _: dict = Depends(require_auth)):
    return {"events": audit_recent(limit=limit)}

@router.post("/agents/execute", response_model=AgentResponse)
def execute_agent(request: AgentRequest, ctx: dict = Depends(require_auth)):
    try:
        return run_request(request, ctx=ctx)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Execution error: {e}") from e
