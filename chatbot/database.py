from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Muat isi file .env
load_dotenv()

# Ambil string koneksi dari environment
uri = os.getenv("MONGODB_CONNECTION_STRING")

# Buat koneksi ke MongoDB
client = MongoClient(uri, server_api=ServerApi('1'))

# Coba ping untuk cek apakah koneksi berhasil
try:
    client.admin.command('ping')
    print("✅ Terkoneksi ke MongoDB Atlas!")
except Exception as e:
    print("❌ Gagal koneksi ke MongoDB:", e)
