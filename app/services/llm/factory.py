from app.core.config import settings
from app.services.llm.groq import GroqLLM

def get_llm():
    if settings.LLM_PROVIDER == "groq":
        return GroqLLM()

    raise ValueError(f"Unsupported LLM: {settings.LLM_PROVIDER}")