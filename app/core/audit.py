from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional
from datetime import datetime

@dataclass
class AuditEvent:
    ts: str
    correlation_id: Optional[str]
    module: str
    crew: str
    task: str
    status: str
    meta: Dict[str, Any]

_AUDIT: List[AuditEvent] = []

def log_event(*, correlation_id: Optional[str], module: str, crew: str, task: str, status: str, meta: Dict[str, Any]):
    _AUDIT.append(
        AuditEvent(
            ts=datetime.utcnow().isoformat() + "Z",
            correlation_id=correlation_id,
            module=module,
            crew=crew,
            task=task,
            status=status,
            meta=meta or {}
        )
    )
    # cap memory
    if len(_AUDIT) > 500:
        del _AUDIT[:-500]

def recent(limit: int = 50) -> List[Dict[str, Any]]:
    return [asdict(e) for e in _AUDIT[-limit:]]