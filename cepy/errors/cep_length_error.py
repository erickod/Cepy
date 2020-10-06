class CepLengthError(Exception):
    _message = 'O cep deve ter exatamente 8 caracteres'
    
    def __init__(self) -> None:
        super(CepLengthError, self).__init__(self._message)