import threading
import time
from bus import EventBus
from events import BookBorrowedEvent
from handlers import MongoSaveHandler, ConsoleNotificationHandler

def main():
    bus = EventBus()
    bus.register_handler(MongoSaveHandler())
    bus.register_handler(ConsoleNotificationHandler())

    thread = threading.Thread(target=bus.start, daemon=True)
    thread.start()

    print("--- KUTUBXONA TIZIMI ---")
    while True:
        # Ma'lumotni foydalanuvchidan so'rash
        book = input("\nKitob nomi (chiqish uchun 'exit'): ")
        if book.lower() == 'exit': break
        
        user = input("Sizning ismingiz: ")
        
        # Voqeani yaratish va yuborish
        event = BookBorrowedEvent(book, user, time.time())
        bus.post_event(event)
        
        time.sleep(1) # Handlerlar ishlashi uchun qisqa vaqt

if __name__ == "__main__":
    main()