from domain.clients import Client
from domain.validators_exceptions import ClientValidatorException, InputError


class Client_Repository:

    def __init__(self):
        self._clients = []

    def get_all_clients(self):
        return self._clients[:]

    def create_client(self, client_id, name):
        if self.find_client_id(client_id) == False:
            new_client = Client(client_id, name)
        else:
            raise ClientValidatorException("There already exists a client with this ID")
        return new_client

    def find_client_id(self, client_id):
        exists = False
        for client in self._clients:
            if str(client_id) == str(client.client_id):
                exists = True
        return exists

    def add_generated_client(self, new_client):
        self._clients.append(new_client)

    def add_new_client(self, new_client):
        self._clients.append(new_client)

    def remove_client(self, client_id):
        for client in self._clients:
            if str(client.client_id) == str(client_id):
                self._clients.remove(client)

    def search_client_id(self,user_input):
        if not user_input.isdigit():
            raise InputError("That was not an integer! :(")
        if self.find_client_id(user_input) == False:
            raise InputError("The client with this ID doesn't exists")

    def replace_client(self, new_client):
        for client in self._clients:
            if str(client.client_id) == str(new_client.client_id):
                client.name = new_client.name
