import re

from cepy.errors import CepInvalidCharacterError
from cepy.interfaces import ValidationInterface


class CepInvalidCharacterValidation(ValidationInterface):
    '''
    Throw an error if len != 8
    '''
    loader_flag = True
    is_active = True
    
    @classmethod
    def validate(cls, cep: str):
        pattern = re.compile(r"(\D)")

        if pattern.search(cep):
            raise CepInvalidCharacterError