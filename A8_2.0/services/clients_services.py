from repository.client_repository import Client_Repository, Client
from random import randint, choice
from domain.validators_exceptions import ClientValidator

class Client_Services:

    def __init__(self, repository: Client_Repository):
        self.__repository = repository
        self.generate_n_clients()

    def generate(self):
        # generate client_id
        client_id_used = []
        client_id = randint(1000, 9999)
        while client_id in client_id_used:
            client_id = randint(1000, 9999)
        client_id_used.append(client_id)

        # generate name
        first_name = ["Alex", "Gloria", "Anne", "John", "Thomas", "Amy", "Aaron", "Michel", "Larisa", "David"]
        last_name = ["Pop", "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Lopez", "Davis"]
        name = choice(first_name) + " " + choice(last_name)

        return self.__repository.create_client(client_id, name)

    def generate_n_clients(self):
        for i in range(20):
            self.__repository.add_generated_client(self.generate())

    def list_clients(self):
        return self.__repository.get_all_clients()

    def add_client(self, client_id, name):
        client = self.__repository.create_client(client_id, name)
        ClientValidator.validate_client(client)
        self.__repository.add_new_client(client)

    def delete_client(self,client_id):
        self.search_client_id_services(client_id)
        self.__repository.remove_client(client_id)

    def update_client(self, client_id, name):
        new_client = Client(client_id, name)
        ClientValidator.validate_client(new_client)
        self.__repository.replace_client(new_client)

    def search_client_id_services(self, client_id):
        self.__repository.search_client_id(client_id)
