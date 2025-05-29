import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

def chat_with_bot(user_message, history=None):
    messages = history if history else []
    messages.append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages
        )
        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply, messages
    except Exception as e:
        print("Error from Groq:", e)
        return "Maaf, terjadi kesalahan saat memproses pesan.", messages
