from abc import ABC, abstractmethod

class ValidationInterface(ABC):

    @abstractmethod
    def validate(self, cep:str) -> bool:
        return False