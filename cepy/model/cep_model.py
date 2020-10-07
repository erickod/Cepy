from cepy.loader import Loader

class Cep: 
    def __init__(self, cep:str, loader=Loader) -> None:
        self.__loader = loader
        self.__init_container()
        self.__validate(cep)
    
    def __init_container(self,) -> None:
        self.__container = {
            'cep':'',
            'state':'',
            'city':'',
            'district':'',
            'address':'',
            'provider':''
        }
    
    @property
    def number(self):
        return self.__container['cep']
    
    @number.setter
    def number(self, cep):
        self.__validate(cep)
        self.__container['cep'] = cep
    
    def __validate(self, cep):
        for rule in self.__loader('cepy/validations').load():
            rule.validate(cep)
        self.__container['cep'] = cep
    
    def __str__(self):
        return f'{self.__container}'
    
    def __repr__(self,):
        return self.__str__()
    
    def __getitem__(self, key):
        if not key in self.__container.keys():
            raise KeyError('Key not allowed')
        return self.__container[key]
    
    def __setitem__(self, key, value):
        if not key in self.__container.keys():
            raise ValueError(f'Assignement not allowed to {key} key')
        if key == 'cep':
            self.__validate(value)
        self.__container[key] = value