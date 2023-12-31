from repository.rental_repository import Rental_Repository, Rental
from repository.client_repository import Client_Repository
from repository.book_repository import Book_Repository
import random
import datetime


class Rental_services:

    def __init__(self, repository: Rental_Repository(), book_repo: Book_Repository(), client_repo: Client_Repository()):
        self.__repository = repository
        self.__book_repo = book_repo
        self.__client_repo = client_repo
        self.generate_n_rentals()


    def generate_rental(self):

        # get book_id
        books_list = self.__book_repo.get_all_books()
        rented_books_id = []
        # get client_id
        clients_list = self.__client_repo.get_all_clients()
        rented_clients_id = []
        # generate rented_id
        book_id = random.choice(books_list).book_id
        while book_id in rented_books_id:
            book_id = random.choice(books_list).book_id
        rented_books_id.append(book_id)

        client_id = random.choice(clients_list)
        while client_id in rented_clients_id:
            client_id = random.choice(clients_list)
        rented_clients_id.append(client_id)

        rented_id = str(book_id) + str(client_id)

        # generate ranted_date and returned date
        rented_date = self.generate_rental_dates()
        # Calculate returned_date as rented_date + 2 weeks
        if datetime.date.today() - rented_date > datetime.timedelta(weeks=2):
            returned_date = rented_date + datetime.timedelta(weeks=2)
            return Rental(rented_id, book_id, client_id, rented_date, returned_date)
        else:
            return Rental(rented_id, book_id, client_id, rented_date)

    def generate_rental_dates(self):
        # Generate a random rented_date within the last year
        start_date = datetime.date.today() - datetime.timedelta(days=365)
        rented_date = self.random_date(start_date)
        return rented_date

    def random_date(self, start_date):
        end_date = datetime.date.today()
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        return random_date

    def generate_n_rentals(self):
        """for i in range(20):
            self.__repository.add_generated_rentals(self.generate())"""
        for i in range(20):
            rental = self.generate_rental()
            if rental:
                self.__repository.add_generated_rentals(rental)

    def available(self, ok):
        books_id = self.__repository.is_rented()
        result = []
        all_books = self.__book_repo.get_all_books()
        print("All Books in available:", all_books)
        if ok == True:
            for book in all_books:
                if str(book.book_id) not in books_id:
                    result.append(book)
        else:
            for book in all_books:
                if str(book.book_id) in books_id:
                    result.append(book)
        return result

    def books_clients(self):
        print("Books in Book_Repository:", self.__book_repo.get_all_books())
        print("Clients in Client_Repository:", self.__client_repo.get_all_clients())

        books_list = self.__book_repo.get_all_books()
        clients_list = self.__client_repo.get_all_clients()
        print(books_list)
        print(clients_list)