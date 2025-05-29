from fastapi import FastAPI, Form
from chatbot.gpt_chat import chat_with_bot

app = FastAPI()

@app.post("/webhook")
async def whatsapp_webhook(
    Body: str = Form(...),
    From: str = Form(...)
):
    user_message = Body
    user_number = From

    print(f"[MASUK] Pesan dari {user_number}: {user_message}")

    bot_reply, _ = chat_with_bot(user_message)

    return f"<Response><Message>{bot_reply}</Message></Response>"
