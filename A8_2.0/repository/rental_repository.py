from domain.rental import Rental

class Rental_Repository:

    def __init__(self):
        self._rentals = []

    def add_generated_rentals(self, rental):
        self._rentals.append(rental)

    def add_rental(self, rental):
        self._rentals.append(rental)

    def get_all_rentals(self):
        return self._rentals[:]

    def is_rented(self):
        books_id = []
        for rent in self._rentals:
            books_id.append(rent.book_id)
        return books_id

