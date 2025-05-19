from repositories import IclienteRepository
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class ClientePersistanceAdapter:
    def __init__(self, cliente_repository: IclienteRepository):

        uri = f"mongodb+srv://luizpauloneto:DOuaCNcwnoRS1gKp@cluster0.25d5slc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            return print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            return print(e)
        
    def get_cliente(self, id: int) -> dict:
        return self.cliente_repository.get_cliente(id)

    def create_cliente(self, cliente: dict) -> dict:
        return self.cliente_repository.create_cliente(cliente)

    def update_cliente(self, id: int, cliente: dict) -> dict:
        return self.cliente_repository.update_cliente(id, cliente)

    def delete_cliente(self, id: int) -> None:
        return self.cliente_repository.delete_cliente(id)