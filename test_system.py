import unittest
import time
from events import BookBorrowedEvent
from bus import EventBus

class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        # Har bir testdan oldin yangi Event Bus yaratamiz
        self.bus = EventBus()

    def test_event_creation(self):
        # Voqea to'g'ri yaratilishini tekshiramiz
        event = BookBorrowedEvent("Test Kitob", "Test Foydalanuvchi", time.time())
        self.assertEqual(event.book_name, "Test Kitob")
        self.assertEqual(event.user_name, "Test Foydalanuvchi")

    def test_bus_registration(self):
        # Handlerlar to'g'ri ro'yxatga olinishini tekshiramiz
        class MockHandler:
            def handle(self, event): pass
        
        handler = MockHandler()
        self.bus.register_handler(handler)
        self.assertIn(handler, self.bus.handlers)

if __name__ == "__main__":
    unittest.main()