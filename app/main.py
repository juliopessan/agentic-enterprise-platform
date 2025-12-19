from fastapi import FastAPI
from app.api.v1.routes import router

app = FastAPI(
    title="Agentic Enterprise Platform",
    version="0.1.0"
)

app.include_router(router, prefix="/v1")

@app.get("/health")
def health():
    return {"status": "ok"}
