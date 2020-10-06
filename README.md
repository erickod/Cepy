# cepy
Uma lib feita em python para consultar cep em diversos serviços

## Serviços disponíveis
- Correios
- ViaCep
- AwesomeApi
- Widenet

## Como utilizar

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


### Quando o cep não é encontrado
```
# {'response': 'Cep não encontrado'}
```

## Observações importantes
- Tudo ainda está sendo desenvolvido, mas é minimamente funcional;
- Faça sugestões, envie pull resquests e ajude o projeto a crescer.
