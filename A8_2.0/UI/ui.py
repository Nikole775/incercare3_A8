from services.book_services import Book_services, Book_Repository
from services.clients_services import Client_Services, Client_Repository
from domain.validators_exceptions import UIerror, BookValidatorException, InputError, ClientValidatorException
from services.rental_services import Rental_Repository, Rental_services
class UI:
    def __init__(self, book_services: Book_services, client_services: Client_Services, rental_services: Rental_services):
        self.__book_services = book_services(Book_Repository())
        self.__client_services = client_services(Client_Repository())
        self.__rental_services = rental_services(Rental_Repository(), Book_Repository(), Client_Repository())
        self.exit_flag = False
        self.menu_level = 0

    def menu(self):
        print("_________________________________________________________________")
        print("1.Manage clients and books.")
        print("2.Rent or return a book.")
        print("3.Search for clients or books ")
        print("4.Statistics")
        print("0.exit")
        print("_________________________________________________________________")

    def manage_clients_books_menu(self):
        print(".................................................................")
        print("1. add a book")
        print("2.remove a book")
        print("3.update a book")
        print("4.list all the books")
        print("5.add a client")
        print("6.remove a client")
        print("7.update a client")
        print("8.list all clients")
        print("0.back")
        print(".................................................................")

    def rent_return_book_menu(self):
        print(".................................................................")
        print("1.list available books")
        print("2.list books that has to be returned")
        print("3.rent a book")
        print("4.return a book")
        print("0.back")
        print(".................................................................")

    def search_clients_books_menu(self):
        print(".................................................................")
        print("1.search a book by id")
        print("2. search a book by title")
        print("3.search a book by author")
        print("4.search a client by id")
        print("5.search a client by name")
        print("0.back")
        print(".................................................................")

    def statistics_menu(self):
        print(".................................................................")
        print("1.most rented books")
        print("2.most active clients")
        print("3.most rented author")
        print("0.back")
        print(".................................................................")

    def get_input (self, txt = "->"):
        return input(txt)

    def choose_option_menu(self,option):
        if option == "1":
            self.menu_level = 1
            self.manage_clients_books()
        elif option == "2":
            self.menu_level = 1
            self.rent_return_book()
        elif option == "0":
            print("You stopped the program. Bye!")
            self.exit_flag = True
        else:
            raise UIerror("That was not a valid option!")

    def manage_clients_books(self):
        while self.menu_level == 1 :
            try:
                self.manage_clients_books_menu()
                option1 = self.get_input()
                self.choose_option_clients_books(option1)
            except UIerror as ve:
                print(ve)

    def rent_return_book(self):
        while self.menu_level == 1:
            try:
                self.rent_return_book_menu()
                option2 = self.get_input()
                self.choose_option_rent_return_book(option2)
            except UIerror as ve:
                print(ve)
    def choose_option_clients_books(self,option):
        if option == "1":
            self.add_book_UI()
        elif option == "2":
            self.remoove_book_UI()
        elif option == "3":
            self.update_book_UI()
        elif option == "4":
            self.list_books_UI()
        elif option == "5":
            self.add_client_UI()
        elif option == "6":
            self.remove_client_UI()
        elif option == "7":
            self.update_client_UI()
        elif option == "8":
            self.list_clients_UI()
        elif option == "0":
            self.menu_level = 0
        else:
            raise UIerror("That was not a valid option!")

    def choose_option_rent_return_book(self, option):
        if option == "1":
            self.list_available_UI()
        elif option == "2":
            self.list_rented_UI()
        elif option == "0":
            self.menu_level = 0
        else:
            raise UIerror("That was not a valid option!")

    def list_books_UI(self):
        print(self.__book_services.list_books())

    def add_book_UI(self):
        try:
            book_id = self.get_input("Book ID: ")
            title = self.get_input("Title: ")
            author = self.get_input("Author: ")
            self.__book_services.add_book(book_id, title, author)
        except BookValidatorException as ve:
            print(ve)

    def remoove_book_UI(self):
        try:
            book_id = self.get_input("Book ID: ")
            self.__book_services.delete_book(book_id)
        except InputError as ve:
            print(ve)

    def update_book_UI(self):
        try:
            book_id = self.get_input("Book ID: ")
            self.__book_services.search_id_services(book_id)
            try:
                title = self.get_input("New Title: ")
                author = self.get_input("New Author: ")
                self.__book_services.update_book(book_id, title, author)
            except BookValidatorException as ve:
                print(ve)
        except InputError as ve:
            print(ve)

    def list_clients_UI(self):
        print(self.__client_services.list_clients())

    def add_client_UI(self):
        try:
            client_id = self.get_input("Client ID: ")
            name = self.get_input("Name: ")
            self.__client_services.add_client(client_id, name)
        except ClientValidatorException as ve:
            print(ve)

    def remove_client_UI(self):
        try:
            client_id = self.get_input("Client ID: ")
            self.__client_services.delete_client(client_id)
        except InputError as ve:
            print(ve)

    def update_client_UI(self):
        try:
            client_id = self.get_input("Client ID: ")
            self.__client_services.search_client_id_services(client_id)
            try:
                name = self.get_input("New Name: ")
                self.__client_services.update_client(client_id, name)
            except ClientValidatorException as ve:
                print(ve)
        except InputError as ve:
            print(ve)

    def list_available_UI(self):
        print(self.__rental_services.available(True))
        self.__rental_services.books_clients()

    def list_rented_UI(self):
        print(self.__rental_services.available(False))

    def start(self):
        while not self.exit_flag:
            try:
                self.menu()
                option = self.get_input()
                self.choose_option_menu(option)
            except UIerror as ve:
                print(ve)



