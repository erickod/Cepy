import typing
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

from cepy.interfaces import ServiceInterface

from cepy.model import Cep
from cepy.services.correios.correios_config import config


class CorreiosService(ServiceInterface):
    __config = config
    __cep_model = Cep
    loader_flag = True
    
    @classmethod
    def get(cls, cep:str) -> Cep:
        model:Cep = cls.__cep_model(cep)
        data = b'<?xml version="1.0"?>\n<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:cli="http://cliente.bean.master.sigep.bsb.correios.com.br/">\n  <soapenv:Header />\n  <soapenv:Body>\n    <cli:consultaCEP>\n      <cep>' + model.number.encode() + b'</cep>\n    </cli:consultaCEP>\n  </soapenv:Body>\n</soapenv:Envelope>'
        req = Request(cls.__config['URL'], data, method='POST')
        response = urlopen(req).read()
        et = ET.fromstring(response.decode('iso-8859-1'))
        return  cls.__fit_to_cep_model(et, model)
    
    @classmethod
    def __fit_to_cep_model(cls, response, cep) -> Cep:
        element = response[0][0][0]

        district = element.find('bairro').text
        cep['district'] = district if district else cep['district']

        city = element.find('cidade').text
        cep['city'] = city if city else cep['city']

        address = element.find('end').text
        cep['address'] = address if address else cep['address']

        state = element.find('uf').text
        cep['state'] = state if state else cep['state']
        cep['provider'] = cls.__name__

        complemento = element.find('complemento2').text
        if complemento:
            cep['address'] += f" {complemento}"
        
        return cep
