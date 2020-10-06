from abc import ABC, abstractmethod
from cepy.model import Cep

class ServiceInterface(ABC):
    
    @abstractmethod
    def get(self, cep:str) -> Cep:
        raise NotImplementedError