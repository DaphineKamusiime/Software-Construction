# main.py
from library import Library
from book_management import EBookManagement

# Standard library usage
library = Library(EBookManagement())
library.add_book("Brave New World")
library.checkout("1", "1001")
