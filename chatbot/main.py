from fastapi import FastAPI, Form
from chatbot.chat_core import chat_with_bot

app = FastAPI()

@app.post("/webhook")
async def whatsapp_webhook(
    Body: str = Form(...),
    From: str = Form(...)
):
    user_message = Body
    user_number = From

    print(f"[MASUK] Pesan dari {user_number}: {user_message}")

    bot_reply = chat_with_bot(user_message, user_number)

    return f"<Response><Message>{bot_reply}</Message></Response>"