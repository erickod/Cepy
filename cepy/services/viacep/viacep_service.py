import json
import re
from urllib.request import Request, urlopen

from cepy.interfaces import ServiceInterface
from cepy.model import Cep
from cepy.services.viacep.viacep_config import config


class ViaCEPService(ServiceInterface):
    __config = config
    __cep_model = Cep
    loader_flag = True
    is_active: bool = True
    
    @classmethod
    def get(cls, cep:str) -> Cep:
        model:Cep = cls.__cep_model(cep)
        url = f"{cls.__config['URL']}/{model.number}/json"
        req = Request(url, method='GET')
        response = json.loads(urlopen(req).read())
        return  cls.__fit_to_cep_model(response, model)
    
    @classmethod
    def __fit_to_cep_model(cls, response, cep) -> Cep:
        cep['state'] = response['uf']
        cep['city'] = response['localidade']
        cep['address'] = response['logradouro']
        cep['district'] = response['bairro']
        cep['provider'] = cls.__name__
        return cep