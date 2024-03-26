# Console-based Library Management System
This is console-based library management system implemented in Python.
Please read through this document to carefully understand how this program works.

## Features
These the functionalities of the system that the client can use to interact with the system.
1.Add a book to the library
2.Remove a book from the library
3.Search for a book by title
4.Search for a book by author
5.Display all books in the library

## How to Use
1.Run the `library.py` script.
2.Follow the on-screen menu to perform library management operations.
3.Input data as prompted.

## SOLID Principles
My sysetem follows the SOLID principles as follows:
**Single Responsibility Principle (SRP)**.Each class has a single responsibility, such as managing books or displaying book lists.
**Open/Closed Principle (OCP)**.The classes are open for extension but closed for modification.
For example, if there is a need to add new features or functionalities to the library system, new classes can be added without modifying the existing ones.
The LibraryManager class can be extended to include new operations or behaviors without changing its existing implementation.
**Liskov Substitution Principle (LSP)**.Inheritance and polymorphism are used appropriately.
The LibraryManager class operates on a list of Book objects. It does not rely on specific implementations of the Book class.
This allows for the substitution of different types of books or book-related classes without affecting the behavior of the LibraryManager
**Interface Segregation Principle (ISP)**.The interfaces are specific to the needs of the clients that use them.In this implementation, there are no explicit interfaces defined. However, the public methods of the LibraryManager class serve as an interface for interacting with the library system.
**Dependency Inversion Principle (DIP)**.Dependency injection is used to invert the dependencies between classes.
The LibraryManager class does not directly instantiate Book objects. Instead, it relies on Book objects being passed to it when performing operations like adding books.
This allows for better decoupling between the LibraryManager class and the Book class, making the system more flexible and easier to maintain.

## Author
`NUWAHEREZA PETER`
