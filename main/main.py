import os
from dotenv import load_dotenv
import openai

load_dotenv()  # baca file .env

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_bot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Kamu adalah asisten pintar yang membantu pengguna dengan pertanyaan seputar [topikmu]."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    print("Bot:", chat_with_bot(user_input))
