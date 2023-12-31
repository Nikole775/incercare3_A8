from UI.ui import Book_services, Book_Repository, UI

book_repo = Book_Repository
book_service = Book_services

ui = UI(book_service)

ui.start()
