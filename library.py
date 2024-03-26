from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_by_title(self, title):
        return [book for book in self.books if book.title.lower()==title.lower()]

    def search_by_author(self, author):
        return [book for book in self.books if book.author.lower()==author.lower()]

    def display_books(self):
        if not self.books:
            print("Seems there are no books in the library!.")
        else:
            print("All books in the library:")
            for i, book in enumerate(self.books):
                print(f"{i+1}.{book.title} by {book.author}")
