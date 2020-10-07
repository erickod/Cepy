import typing

from cepy.interfaces import TransformInterface


class CepFillTransform(TransformInterface):
    '''
    Fill cep with 0 if len < 8
    '''
    loader_flag = True
    
    @classmethod
    def transform(cls, cep: typing.Union[str, int]) -> str:
        max_length = 7
        cep = str(cep)
        cep_length = len(cep) -1
        fill = ''.join([str(0) for _ in range(0, max_length - cep_length)])
        cep = ''.join([fill, cep])
        return cep