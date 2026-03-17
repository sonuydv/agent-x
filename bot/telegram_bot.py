import httpx
from app.core.config import settings

async def send_message(chat_id: int, text: str):
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage"

    async with httpx.AsyncClient() as client:
        await client.post(url, json={
            "chat_id": chat_id,
            "text": text
        })