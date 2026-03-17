from fastapi import APIRouter, Request

from bots.telegram.telegram_bot import send_message
from bots.telegram.telegram_message import TelegramMessage

router = APIRouter()

@router.post("/webhook")
async def telegram_webhook(req: Request):
    req_data = await req.json()
    data = TelegramMessage(**req_data)

    print(data)

    if not data.message.text:
        return {"ok": True}

    # response = await generate_response(text)

    await send_message(data.message.chat.id, "hello")

    return {"ok": True}