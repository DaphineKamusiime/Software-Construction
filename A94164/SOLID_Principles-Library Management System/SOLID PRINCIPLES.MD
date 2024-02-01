# SOLID Principles in Library Management System

The Library Management System demonstrates the application of SOLID principles in a Python codebase, ensuring a robust, maintainable, and scalable software architecture. Below is an overview of how each principle is applied:

## Single Responsibility Principle (SRP)

- **BookManagement**, **NotificationManager**, and **ActivityLogger** each handle a single responsibility.
  - `BookManagement` manages book-related operations.
  - `NotificationManager` handles the sending of notifications.
  - `ActivityLogger` is responsible for logging activities.

## Open/Closed Principle (OCP)

- The system is designed to be open for extension but closed for modification.
  - New types of book management (e.g., **EBookManagement**) can be added without altering the existing code, showcasing how new functionalities can be introduced with minimal changes to the existing system.

## Liskov Substitution Principle (LSP)

- **EBookManagement** is a subclass of **BookManagement** and can be substituted without altering the correctness of the program.
  - This ensures that the **Library** class can operate with any implementation of **BookManagement**, providing flexibility and promoting reuse.

## Interface Segregation Principle (ISP)

- Abstract base classes (e.g., **BookManagement**) act as interfaces, ensuring that **Library** interacts only with the necessary operations it requires.
  - This principle prevents the "fat interface" problem by segregating interfaces so that classes don't depend on methods they don't use.

## Dependency Inversion Principle (DIP)

- **Library** depends on abstractions (**BookManagement**) rather than concrete implementations.
  - This inversion of dependency enhances modularity and makes the system more adaptable to changes, such as introducing different strategies for managing books without affecting the **Library**'s operation.

### Example Usage

```python
if __name__ == "__main__":
    library = Library(EBookManagement())
    library.add_book("Brave New World")
    library.checkout("1", "1001")
    library.return_book("1", "1001")
    library.send_overdue_notices()
    library.log_activity("End of day activities.")
```
