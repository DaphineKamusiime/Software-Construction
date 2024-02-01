# library.py
from book_management import BookManagement, EBookManagement
from notification_manager import NotificationManager
from activity_logger import ActivityLogger

class Library:
    def __init__(self, book_management: BookManagement):
        self.book_management = book_management
        self.notification_manager = NotificationManager()
        self.activity_logger = ActivityLogger()

    def checkout(self, book_id, user_id):
        self.book_management.checkout(book_id, user_id)
        self.activity_logger.log_activity(f"Book {book_id} checked out by User {user_id}")

    def return_book(self, book_id, user_id):
        self.book_management.return_book(book_id, user_id)
        self.activity_logger.log_activity(f"Book {book_id} returned by User {user_id}")

    def add_book(self, book):
        self.book_management.add_book(book)
        self.activity_logger.log_activity(f"New book added: {book}")

    def send_overdue_notices(self):
        self.notification_manager.send_overdue_notices()
        self.activity_logger.log_activity("Overdue notices sent")

    def log_activity(self, activity):
        self.activity_logger.log_activity(activity)
