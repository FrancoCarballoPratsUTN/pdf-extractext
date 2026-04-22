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

def get_collection():
    return collection