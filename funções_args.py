### Funções *args são utilizadas quando não sabemos o numero de
# argumentos necessarios em uma função
# deixamos isso flexivel (em aberto)
# O retorno ou saida dessa função retorna uma tupla

def soma(*args):
    print(args)


soma(1,2,3,4,5,6,7,8,9)

def soma_total(*args):
    total = 0
    for n in args:
        total = n+total
    return total


print(soma_total(1,2,3,4,5))