## funções decoradoras servem para potencializar (dar mais recursos)
## para outras funções
## para utilizar uma função decoradora, ultiliza o @ antes do nome da função
## e acima da função que sera decorada (receberá os poderes da outra função)

## Criar função decoradora 

def master(msg):
    def imprime():
        print("Essa é uma função decoradora")
        msg()
    return imprime


## segunda função que vai ser utilizada junto com a decoradora

@master
def funcao_simples():
    print("estou chamando a função simples")


funcao_simples()