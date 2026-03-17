from app.services.llm.factory import get_llm

llm = get_llm()

async def generate_response(prompt: str) -> str:
    return await llm.generate(prompt)