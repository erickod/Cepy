from cepy.errors import CepLengthError
from cepy.interfaces import ValidationInterface


class CepLengthValidation(ValidationInterface):
    '''
    Throw an error if len != 8
    '''
    loader_flag = True
    is_active = True
    
    @classmethod
    def validate(cls, cep_model):
        if not len(cep_model) == 8:
            raise CepLengthError