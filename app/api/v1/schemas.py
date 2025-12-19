from pydantic import BaseModel, Field
from typing import Any, Dict, Optional, Literal

ModuleName = Literal["hr", "finance"]

class Approval(BaseModel):
    required: bool = False
    threshold: float = 0.0
    amount_field: str = "amount"
    approved: bool = False
    approver: Optional[str] = None

class AgentRequest(BaseModel):
    module: ModuleName
    crew: str = Field(..., description="Crew identifier (e.g., TalentOpsCrew)")
    agent: Optional[str] = Field(None, description="Optional agent identifier")
    task: str = Field(..., description="Task name to run")
    payload: Dict[str, Any] = Field(default_factory=dict)
    autonomy_level: str = Field("L1", description="L0..L3")
    correlation_id: Optional[str] = Field(None, description="Trace id for audit/observability")
    approval: Optional[Approval] = Field(default=None, description="Human-in-the-loop controls")

class AgentResponse(BaseModel):
    correlation_id: Optional[str] = None
    module: ModuleName
    crew: str
    task: str
    result: Any
    meta: Dict[str, Any] = Field(default_factory=dict)
