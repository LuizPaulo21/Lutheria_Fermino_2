from abc import ABC, abstractmethod
from typing import List

#Interface for cliente repository
# This interface defines the methods that any concrete implementation of the cliente repository must implement.
class IclienteRepository(ABC):

    @abstractmethod
    def get_cliente(self, id: int) -> dict:
        pass
    
    @abstractmethod
    def create_cliente(self, cliente: dict) -> dict:
        pass

    @abstractmethod
    def update_cliente(self, id: int, cliente: dict) -> dict:
        pass

    @abstractmethod
    def delete_cliente(self, id: int) -> None:
        pass