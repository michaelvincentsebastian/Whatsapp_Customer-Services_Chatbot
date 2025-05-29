import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_bot(user_message, history=None):
    messages = history if history else []
    messages.append({"role": "user", "content": user_message})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = response['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": reply})
        return reply, messages
    except Exception as e:
        print("Error from OpenAI:", e)
        return "Maaf, terjadi kesalahan saat memproses pesan.", messages