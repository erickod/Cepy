import json
import re
from urllib.request import Request, urlopen

from cepy.interfaces import ServiceInterface
from cepy.model import Cep
from cepy.services.cepla.cepla_config import config


class CepLaService(ServiceInterface):
    __config = config
    __cep_model = Cep
    loader_flag = True
    is_active: bool = True
    
    @classmethod
    def get(cls, cep:str) -> Cep:
        headers = {'Accept': 'application/json'}
        model:Cep = cls.__cep_model(cep)
        url = f"{cls.__config['URL']}/{model.number}"
        req = Request(url, method='GET', headers=headers)
        response = json.loads(urlopen(req).read())
        return  cls.__fit_to_cep_model(response, model)
    
    @classmethod
    def __fit_to_cep_model(cls, response, cep) -> Cep:
        cep['state'] = response['uf']
        cep['city'] = response['cidade']
        cep['address'] = response['logradouro']
        cep['district'] = response['bairro']
        cep['provider'] = cls.__name__
        return cep