from ollama import Client

client = Client()  # default: localhost:11434

# Penyimpanan histori lokal per sesi (bisa diperluas nanti)
session_history = {}

def get_history(user_number):
    return session_history.get(user_number, [])

def save_message(user_number, sender, message):
    print(f"[{sender.upper()}] {user_number}: {message}")
    if user_number not in session_history:
        session_history[user_number] = []
    role = "user" if sender == "user" else "assistant"
    session_history[user_number].append({"role": role, "content": message})

def chat_with_bot(user_message, user_number):
    messages = get_history(user_number)
    save_message(user_number, "user", user_message)

    try:
        response = client.chat(
            model="llama3",
            messages=messages + [{"role": "user", "content": user_message}]
        )
        reply = response['message']['content']
        save_message(user_number, "bot", reply)
        return reply
    except Exception as e:
        print("Error from Ollama:", e)
        return "Maaf, terjadi kesalahan saat memproses pesan."