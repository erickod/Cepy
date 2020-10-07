import re

from cepy.errors import CepInvalidCharacterError
from cepy.interfaces import ValidationInterface


class CepInvalidCharacterValidation(ValidationInterface):
    '''
    Throw an error if theres is invalid characters
    '''
    loader_flag = True
    
    @classmethod
    def validate(cls, cep: str):
        pattern = re.compile(r"(\D)")

        if pattern.search(cep):
            raise CepInvalidCharacterError