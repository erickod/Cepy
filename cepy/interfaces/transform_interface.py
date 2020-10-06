from abc import ABC, abstractmethod

class TransformInterface(ABC):

    @abstractmethod
    def transform(self, cep:str) -> str:
        return ''