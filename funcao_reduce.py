### Função reduce serve para reduzi os valores de uma estrutura de dados a um unico valor

# precisamos importar um modulo  builtin chamado functools

from functools import reduce 

lista = [1,2,3,4,5,6]

def mult(x,y):
    return x*y

print(reduce(mult,lista))

# Testar o maior valor usando o redue

lista2 = [14,56,73,98,34]

testmaior = lambda x,y: x if (x>y) else y

print(reduce(testmaior,lista2))