from groq import AsyncGroq

from app.services.llm.base import BaseLLM
from app.core.config import settings

class GroqLLM(BaseLLM):
    def __init__(self):
        self.client = AsyncGroq(api_key=settings.GROQ_API_KEY)

    async def generate(self, prompt: str) -> str:
        res = await self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return res.choices[0].message.content