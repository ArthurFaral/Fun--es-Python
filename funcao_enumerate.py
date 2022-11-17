### Função enumerate enumera indices de estruturas de dados
# retornar o indice de uma lista

animais = ["chachorro","gato","periquito","cavalo"]

print(list(enumerate(animais)))

## Iterador com o enumarate

for i,valor in enumerate(animais):
    print(i,valor)

# Iterador e enumerate com condicionais

for i,valor in enumerate(animais):
    if i>1:
        break
else:
    print(valor)
