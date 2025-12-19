import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    # Auth
    api_token: str = os.getenv("API_TOKEN", "")  # simple bearer for MVP; replace with OAuth/Azure AD later
    # LLM
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    # Runtime
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    environment: str = os.getenv("ENVIRONMENT", "dev")

settings = Settings()
