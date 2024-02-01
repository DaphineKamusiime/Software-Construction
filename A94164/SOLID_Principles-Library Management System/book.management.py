# book_management.py

class BookManagement:
    def checkout(self, book_id, user_id):
        print(f"Checking out book {book_id} to user {user_id}")
        # Checkout logic ...

    def return_book(self, book_id, user_id):
        print(f"Returning book {book_id} from user {user_id}")
        # Return logic ...

    def add_book(self, book):
        print(f"Adding new book: {book}")
        # Add book logic ...

class EBookManagement(BookManagement):
    def checkout(self, book_id, user_id):
        print(f"Checking out e-book {book_id} to user {user_id}")
        # Specific logic for checking out e-books ...
