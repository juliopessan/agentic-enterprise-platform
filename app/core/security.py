from fastapi import HTTPException
from typing import Optional, Dict, Any
from app.core.config import settings

def require_bearer(authorization: Optional[str]) -> None:
    if not settings.api_token:
        # allow in dev/local only
        if settings.environment.lower() in ("dev", "local"):
            return
        raise HTTPException(status_code=500, detail="API_TOKEN not configured on server")

    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing Bearer token")

    token = authorization.split(" ", 1)[1].strip()
    if token != settings.api_token:
        raise HTTPException(status_code=403, detail="Invalid token")

def auth_context(authorization: Optional[str]) -> Dict[str, Any]:
    require_bearer(authorization)
    return {"auth": "bearer", "tenant": "default", "user": "api-client"}