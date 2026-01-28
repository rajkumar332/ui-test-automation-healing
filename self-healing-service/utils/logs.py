import datetime

def log_event(collection, event):
    event["timestamp"] = datetime.datetime.utcnow()
    collection.insert_one(event)
