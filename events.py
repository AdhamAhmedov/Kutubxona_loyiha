
from dataclasses import dataclass

@dataclass
class BookBorrowedEvent:
    book_name: str
    user_name: str
    timestamp: float