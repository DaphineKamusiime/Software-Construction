#Library managment system
class Library:
    def checkout(self, book_id, user_id):
        # Checkout logic
        pass

    def return_book(self, book_id, user_id):
        # Return logic
        pass

    def add_book(self, book):
        # Add book logic
        pass

    def send_overdue_notices(self):
        # Send notices logic
        pass

    def log_activity(self, activity):
        # Logging logic
        pass

#Extract Book Management Functions
class BookManagement:
    def checkout(self, book_id, user_id):
        # Checkout logic
        pass

    def return_book(self, book_id, user_id):
        # Return logic
        pass

    def add_book(self, book):
        # Add book logic
        pass

#Extract Notification Functions
class NotificationManager:
    def send_overdue_notices(self):
        # Send notices logic
        pass
