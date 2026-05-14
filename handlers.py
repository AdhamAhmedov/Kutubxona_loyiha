import time
from pymongo import MongoClient
from events import BookBorrowedEvent

class MongoSaveHandler:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["kutubxona_db"]
        self.collection = self.db["voqealar_tarixi"]

    def handle(self, event):
        if isinstance(event, BookBorrowedEvent):
            data = {
                "event_type": "Kitob olindi",
                "book": event.book_name,
                "user": event.user_name,
                "date": time.ctime(event.timestamp)
            }
            self.collection.insert_one(data)
            print(f"\n✅ MongoDB: '{event.book_name}' saqlandi.")

class ConsoleNotificationHandler:
    def handle(self, event):
        if isinstance(event, BookBorrowedEvent):
            print(f"📢 Bildirishnoma: {event.user_name} kitob oldi.")