from pymongo import MongoClient
from dotenv import load_dotenv
import os

env = load_dotenv()
host = os.getenv("MONGO_HOST")
port = os.getenv("MONGO_PORT")
user = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASSWORD")


client = MongoClient(host=host, port=port, username=user, password=password)
db = client['pdf_extractext']
collection = db["file"]
collection.create_index("mi_llave_unica", unique=True)

def get_collection():
    return collection