from pymongo import MongoClient

client = MongoClient("your_mongodb_atlas_connection_string")
db = client['chatbot_db']
sessions = db['sessions']

def get_messages(session_id):
    session = sessions.find_one({"session_id": session_id})
    if session:
        return session['messages']
    else:
        # buat baru kalau belum ada
        sessions.insert_one({"session_id": session_id, "messages": []})
        return []

def save_message(session_id, role, content):
    sessions.update_one(
        {"session_id": session_id},
        {"$push": {"messages": {"role": role, "content": content}}},
        upsert=True
    )
