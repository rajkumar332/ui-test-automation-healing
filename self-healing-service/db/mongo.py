import os
from pymongo import MongoClient

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)
db = client["locator_healing"]

elements = db["elements"]
history = db["history"]
