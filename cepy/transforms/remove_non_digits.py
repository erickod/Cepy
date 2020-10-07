import re
import typing

from cepy.interfaces import TransformInterface


class RemoveNonDigitsTransform(TransformInterface):
    '''
    Remove everything that don't matches with digits
    '''
    loader_flag = True
    
    @classmethod
    def transform(cls, cep: typing.Union[str, int]) -> str:
        pattern = re.compile(r'\d')
        cep = str(cep)
        cep_list: typing.List[str] = [char for char in cep if pattern.match(char)]
        return ''.join(cep_list)