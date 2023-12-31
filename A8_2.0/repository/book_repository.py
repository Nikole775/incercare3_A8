from domain.book import Book
from domain.validators_exceptions import InputError, BookValidatorException


class Book_Repository:

    def __init__(self):
        self._books = []

    def get_all_books(self):
        return self._books[:]

    def create_book(self, book_id, title, author):
        if self.find_book_id(book_id) == False:
            new_book = Book(book_id, title, author)
        else:
            raise BookValidatorException("There already exists a book with this ID")
        return new_book

    def add_generated_book(self, new_book):
        self._books.append(new_book)

    def find_book_id(self, book_id):
        exists = False
        for book in self._books:
            if str(book_id) == str(book.book_id):
                exists = True
        return exists

    def add_new_book(self, book):
        self._books.append(book)

    def remove_book(self, book_id):
        for book in self._books:
            if str(book.book_id) == str(book_id):
                self._books.remove(book)

    def replace_book(self, new_book):
        for book in self._books:
            if str(book.book_id) == str(new_book.book_id):
                book.title = new_book.title
                book.author = new_book.author

    def search_id(self, user_input):
        if not user_input.isdigit():
            raise InputError("That was not an integer! :(")
        if self.find_book_id(user_input) == False:
            raise InputError("The book with this ID doesn't exists")

    def find_all_books(self):
        return list(self._books.values())
