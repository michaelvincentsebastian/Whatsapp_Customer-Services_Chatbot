from fastapi import FastAPI, Request, Form
from gpt_chat import chat_with_bot
from database import save_message
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

@app.post("/webhook")
async def whatsapp_webhook(
    Body: str = Form(...),
    From: str = Form(...)
):
    user_message = Body
    user_number = From

    print(f"Pesan dari {user_number}: {user_message}")

    # Proses dengan OpenAI
    bot_reply = chat_with_bot(user_message)

    # Simpan ke MongoDB
    save_message(user_number, "user", user_message)
    save_message(user_number, "bot", bot_reply)

    # Kirim balasan kembali
    return f"<Response><Message>{bot_reply}</Message></Response>"
