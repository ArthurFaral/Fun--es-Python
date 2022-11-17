### Funções são blocos ou códigos criados de forma pré determinada onde executa uma ação
# Sempre que precisarmos dela, chamamos a função ou se precisarmos repetir determinadas ações 

## Função sem argumentos (sem parametros ou argumentos)

def oi():
    print("Ola estou dando oi")

    #chamando a função

oi()


#Funçãocom argumentos ou parametros 

def soma(a,b):
    return a+b

print(soma(1,3))

###################################################################################################################

#def soma(a,b=4):

#dará 5 pois a máquina ira entender que o b sera 4, mesmo não estando fisivelmente lá

#print(soma(1))