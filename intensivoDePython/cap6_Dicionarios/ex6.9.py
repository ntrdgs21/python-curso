lugares_favoritos = {
    'nathan':{
        'Opção1':'Nova Zelandia',
        'Opção2':'EUA',
        'Opção3':'Suíça'
    },
    'ariadne':{
        'Opção1':'EUA',
        'Opção2':'Canadá',
        'Opção3': 'Holanda'
    },
    'marjorie': {
        'Opção1':'Brasil',
        'Opção2':'Portugal',
        'Opção3':'Espanha'
    }
}

for chave,valor in lugares_favoritos.items():
    print(f"{chave.title()} tem as seguintes opções:")
    for opcao,pais in valor.items():
        print(f"{opcao} é {pais}")