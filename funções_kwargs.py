# Funções kwargs
# passar um numero  indeterminado de parametros  para uma função 
# Mas diferente do *args, vocêprecisa passar nos argumentos, o identificador
# de chaves e valores 

def saudacoes(**kwargs):
    print(kwargs)

saudacoes(manha='bom dia')


def saudacao_dia(**kwargs):
    for periodo_dia,saudacao in kwargs.items():
        print(f'Durante a {periodo_dia} dizemos {saudacao}') #fstring

        # chamar a função

saudacao_dia(manha='bom dia',tarde='boa tarde',noite='boa noite')