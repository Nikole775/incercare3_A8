from repository.book_repository import Book_Repository, Book
from random import randint, choice
from domain.validators_exceptions import BookValidator


class Book_services:

    def __init__(self, repository: Book_Repository):
        self.__repository = repository
        self.generate_n_books()

    def generate(self):
        # generate book_id
        book_id_used = []
        book_id = randint(1000, 9999)
        while book_id in book_id_used:
            book_id = randint(1000, 9999)
        book_id_used.append(book_id)

        # generate title

        titles = ["Pride and Prejudice", "1984", "Crime and Punishment", "Hamlet", "One Hundred Years of Solitude",
                  "Anna Karenina", "The Odyssey", "The Stranger", "The Brothers Karamazov", "Lolita",
                  "The Old Man and The Sea", "War and Peace", "Great Expectations", "Don Quixote", "The Iliad",
                  "Madame Bovary", "The Trial"]
        title = choice(titles)

        # generate authors
        names = ["Jane Austen", "George Orwell", "Fyodor Dostoevsky", "William Shakespeare", "Gabriel Garcia",
                 "Leo Tolstoy", "Homer", "Albert Camus", "Vladimir Nabokov", "Ernest Hemingway", "Charles Dickens",
                 "Miguel de Cervantes", "Gustave Flaubert", "Franz Kafka", "Dante Alighieri", "Herman Melville"]
        author = choice(names)

        return self.__repository.create_book(book_id, title, author)

    def generate_n_books(self):
        for i in range(20):
            self.__repository.add_generated_book(self.generate())

    def delete_book(self,book_id):
        self.__repository.search_id(book_id)
        self.__repository.remove_book(book_id)

    def verify_id(self,book_id):
        return self.__repository.find_book_id(book_id)

    def list_books(self):
        return self.__repository.get_all_books()

    def add_book(self, book_id, title, author):
        book = self.__repository.create_book(book_id, title, author)
        BookValidator.validate_book(book)
        self.__repository.add_new_book(book)

    def update_book(self, book_id, title, author):
        new_book = Book(book_id, title, author)
        BookValidator.validate_book(new_book)
        self.__repository.replace_book(new_book)

    def search_id_services(self, book_id):
        self.__repository.search_id(book_id)
