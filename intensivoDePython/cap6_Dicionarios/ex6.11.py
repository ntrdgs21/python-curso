cidades = {
    'rio de janeiro':{
        'país':'brasil',
        'população': '6.211 m',
        'fato': 'primeira cidade do brasil'
    },
    'toronto':{
    'país':'canadá',
    'população':'3,026 m',
    'fato':'maior cidade do canadá'
    },
    'orlando':{
    'país':'eua',
    'população':'2 m',
    'fato':'cidade onde há o maior número de parques de diversão no mundo'
    }
}

for cidades,informacoes in cidades.items():
    print(cidades.title())
    for chave,valor in informacoes.items():
        print(f"{chave} : {valor}\n")