from fastapi import APIRouter, Request

from app.services.llm.llm_service import generate_response
from bot.telegram_bot import send_message

router = APIRouter()

@router.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()

    message = data.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text")

    if not text:
        return {"ok": True}

    response = await generate_response(text)

    await send_message(chat_id, response)

    return {"ok": True}