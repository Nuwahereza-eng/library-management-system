from book import Book
from library import Library

def main():
    library = Library()
    while True:
        print("Library Management System Menu:")
        print("1.Add a book")
        print("2.Remove a book")
        print("3.Search for a book by title")
        print("4.Search for a book by author")
        print("5.Display all books")
        print("6.Exit")

        choice = input("Enter your choice: ")
        if choice =="1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            book = Book(title, author)
            library.add_book(book)
            print("Book added successfully.")

        elif choice =="2":
            title = input("Enter the title of the book to remove: ")
            books_found = library.search_by_title(title)
            if books_found:
                for i, book in enumerate(books_found, 1):
                    print(f"{i}. {book.title} by {book.author}")
                index = int(input("Enter the number of the book to remove: ")) - 1
                library.remove_book(books_found[index])
                print("Book removed successfully.")
            else:
                print("Book not found.")

        elif choice =="3":
            title = input("Enter the title of the book to search: ")
            books_found = library.search_by_title(title)
            if books_found:
                print("Books found:")
                for book in books_found:
                    print(f"{book.title} by {book.author}")
            else:
                print("No books found with that title.")

        elif choice =="4":
            author = input("Enter the author of the book to search: ")
            books_found = library.search_by_author(author)
            if books_found:
                print("Books found:")
                for book in books_found:
                    print(f"{book.title} by {book.author}")
            else:
                print("No books found by that author.")

        elif choice =="5":
            library.display_books()

        elif choice =="6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__=="__main__":
    main()
