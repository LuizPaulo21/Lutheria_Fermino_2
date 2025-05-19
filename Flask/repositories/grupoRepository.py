from abc import ABC, abstractmethod
from typing import List

#Class para interface de grupo repository
# This interface defines the methods that any concrete implementation of the grupo repository must implement.
class IgrupoRepository(ABC):

    @abstractmethod
    def get_grupo(self, id: int) -> dict:
        pass
        
    @abstractmethod
    def create_grupo(self, grupo: dict) -> dict:
        pass

    @abstractmethod
    def update_grupo(self, id: int, grupo: dict) -> dict:
        pass

    @abstractmethod
    def delete_grupo(self, id: int) -> None:
        pass