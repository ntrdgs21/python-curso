pets = []
animais = {
    'bolt':{
        'raça': 'yorkshire',
        'dono': 'marjorie'
    },
    'paco': {
        'raça': 'siames',
        'dono': 'maria'
    },
    'mickey':{
        'raça':'porquinho da índia',
        'dono': 'nathan'
    }
}
pets.append(animais)

for grupo in pets:
    for animal, dados in grupo.items():
        print(f"\n{animal.title()} com os seguintes dados:")
        for chave, valor in dados.items():
            print(f"  {chave.title()}: {valor.title()}")