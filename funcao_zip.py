## zip ela manipula e mescla estrutura dedos e seus valores
## porem o resultado sempre será o valor da menor estrutura


dicverduras = {1: "cebola", 2: "alface",3: "batata",4: "beterraba"}
dicfrutas = {1:"maça",2: "banana",3: "uva", 4: "pera"} 

mescla = list(zip(dicverduras,dicfrutas))

print(mescla)


mesclavalores = list(zip(dicverduras.values(),dicfrutas.values()))

print(mesclavalores)

#alterar os valores

for p in mesclavalores:
    print(p)