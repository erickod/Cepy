class ReturnProcessingError(Exception):
    _message = 'Não foi possível processar o retorno'
    
    def __init__(self) -> None:
        super(ReturnProcessingError, self).__init__(self._message)