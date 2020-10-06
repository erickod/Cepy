class CepInvalidCharacterError(Exception):
    _message = 'O Cep possui caracteres inválidos'
    
    def __init__(self) -> None:
        super(CepInvalidCharacterError, self).__init__(self._message)