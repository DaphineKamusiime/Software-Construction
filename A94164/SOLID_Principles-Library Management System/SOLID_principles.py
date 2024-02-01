from abc import ABC, abstractmethod

# Interface Segregation Principle (ISP) and Dependency Inversion Principle (DIP) are demonstrated
# through the use of abstract base classes (ABCs) and their implementations.

class BookManagement(ABC):
    @abstractmethod
    def checkout(self, book_id, user_id):
        pass

    @abstractmethod
    def return_book(self, book_id, user_id):
        pass

    @abstractmethod
    def add_book(self, book):
        pass

class EBookManagement(BookManagement):
    def checkout(self, book_id, user_id):
        print(f"Checking out e-book {book_id} to user {user_id}.")
        # E-book specific checkout logic

    def return_book(self, book_id, user_id):
        print(f"Returning e-book {book_id} from user {user_id}.")
        # Inherit or override as needed

    def add_book(self, book):
        print(f"Adding new e-book: {book}.")
        # E-book specific add logic

class NotificationManager:
    def send_overdue_notices(self):
        print("Sending overdue notices...")
        # Notification logic

class ActivityLogger:
    def log_activity(self, activity):
        print(f"Activity Log: {activity}")
        # Logging logic

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

# Example Usage
if __name__ == "__main__":
    # Using the Library with standard book management
    library = Library(EBookManagement())
    library.add_book("Brave New World")
    library.checkout("1", "1001")
    library.return_book("1", "1001")
    library.send_overdue_notices()
    library.log_activity("End of day activities.")


'''USE OF SOLID PRINCIPLES:Explanation
Single Responsibility Principle (SRP): Each class has a single responsibility (managing books, sending notifications, logging activities).
Open/Closed Principle (OCP): The system is open for extension (e.g., adding new types of book management like EBookManagement) without modifying existing code.
Liskov Substitution Principle (LSP): EBookManagement can be substituted for BookManagement without altering the desirable properties of the program (i.e., Library works with any BookManagement implementation).
Interface Segregation Principle (ISP): By using abstract base classes, we ensure that the Library depends only on the interfaces it requires (e.g., the abstract methods in BookManagement), not on unnecessary details.
Dependency Inversion Principle (DIP): Library depends on the abstract BookManagement rather than concrete implementations, allowing for easy swapping of different book management strategies.'''