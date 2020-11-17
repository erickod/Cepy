# cepy
Uma lib feita em python para consultar cep em diversos serviços

## Serviços disponíveis
- AwesomeApi
- Cep.la
- Correios
- ViaCep
- Widenet

## Como utilizar
No mesmo diretório onde está o example.py execute o código abaixo:

```
from cepy import Cepy

cep = Cepy()
print(cep(21351050))
```

### Quando o cep é encontrado
```
# {'cep': '21351050', 'state': 'RJ', 'city': 'Rio de Janeiro', 'district': 'Madureira', 
# 'address': 'Estrada do Portela - até 279 - lado ímpar', 'provider': 'CorreiosService'}
```
### Consultando todos os serviços
```
from cepy import Cepy

cep = Cepy()
print(cep(21351050, get_all=True))
```

```
#[{'cep': '01513000', 'state': 'SP', 'city': 'São Paulo', 'district': 'Liberdade', 'address': 'Rua São Paulo', 
#'provider': 'CepLaService'}, {'cep': '01513000', #'state': 'SP', 'city': 'São Paulo', 'district': 'Liberdade', 
#'address': 'Rua São Paulo', 'provider': 'AwesomeApiService'}, {'cep': '01513000', 'state': 'SP', #'city': 'São Paulo', 
#'district': 'Liberdade', 'address': 'Rua São Paulo', 'provider': 'ViaCEPService'}, {'cep': '01513000', 'state': 'SP', 
#'city': 'São Paulo', #'district': 'Liberdade', 'address': 'Rua São Paulo', 'provider': 'WideNetService'}, 
#{'cep': '01513000', 'state': 'SP', 'city': 'São Paulo', 'district': #'Liberdade', 'address': 'Rua São Paulo', 
#'provider': 'CorreiosService'}]
```

### Quando o cep não é encontrado
```
# {'response': 'Cep não encontrado'}
```
