from UI.ui import Book_services, Book_Repository, UI, Client_Services, Client_Repository, Rental_Repository, Rental_services

"""book_repo = Book_Repository
book_service = Book_services

client_repo = Client_Repository
client_service = Client_Services

rent_repo = Rental_Repository
rent_service = Rental_services

ui = UI(book_service, client_service, rent_service)

ui.start()"""

class LibraryApp:
    def __init__(self):
        # Initialize repositories
        book_repo = Book_Repository
        client_repo = Client_Repository
        rental_repo = Rental_Repository

        # Initialize services with repositories
        book_service = Book_services
        client_service = Client_Services
        rental_service = Rental_services

        # Initialize UI with services
        ui = UI(book_service, client_service, rental_service)

        # Start the application
        ui.start()

if __name__ == "__main__":
    app = LibraryApp()
