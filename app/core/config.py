import os

from pydantic.v1 import BaseSettings

class Settings(BaseSettings):
    APP_ENV: str = "dev"

    TELEGRAM_TOKEN: str

    LLM_PROVIDER: str = "groq"
    GROQ_API_KEY: str | None = None

    DB_PROVIDER: str = "sqlite"

    class Config:
        env_file = ".env" if os.path.exists(".env") else None
        case_sensitive = True

settings = Settings()