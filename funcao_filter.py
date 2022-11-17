## A função FILTER, filtra um valor da estrututra de dados


lista1 = [19,'Arthur', 18, 'Theo']

def busca(x):
    return x == 'Arthur'

print(list(filter(busca,lista1)))


## Otimizando a busca utilizando LAMBDA


print(list(filter(lambda x: x+ 'Arthur',lista1)))