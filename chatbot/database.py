# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
from dotenv import load_dotenv
# import os
from datetime import datetime

load_dotenv()

# uri = os.getenv("MONGODB_CONNECTION_STRING")
# client = MongoClient(uri, server_api=ServerApi('1'))

# db = client["chatbot"]
# collection = db["messages"]

# try:
#     client.admin.command('ping')
#     print("\u2705 Terkoneksi ke MongoDB Atlas!")
# except Exception as e:
#     print("\u274C Gagal koneksi ke MongoDB:", e)

def save_message(user_number, sender, message):
    # Simulasi penyimpanan lokal
    print(f"[SIMULASI] Simpan: {user_number} - {sender} - {message} - {datetime.utcnow()}")

def get_history(user_number):
    # Simulasi histori kosong
    print(f"[SIMULASI] Ambil histori untuk: {user_number}")
    return []
