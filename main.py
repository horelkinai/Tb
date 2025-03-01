import os
import json
import logging
from fastapi import FastAPI, Request
from telegram import Bot
from telegram.constants import ParseMode

# Получаем токен Telegram-бота из переменных окружения
TELEGRAM_BOT_TOKEN = os.getenv("7704033906:AAEA602qFco387f4YMJbZ_7Pe63XnFWK6as")
CHAT_ID = os.getenv("6707689636")  # ID чата или канала, куда отправлять сообщения

bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Создаём сервер
app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    try:
        data = await request.json()
        message = f"📊 *TradingView Alert!*\n\n🔹 *Symbol:* {data.get('ticker', 'N/A')}\n🔹 *Price:* {data.get('close', 'N/A')}\n🔹 *Message:* {data.get('message', 'No message')}"
        
        await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=ParseMode.MARKDOWN)
        return {"status": "ok"}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": "error", "message": str(e)}
