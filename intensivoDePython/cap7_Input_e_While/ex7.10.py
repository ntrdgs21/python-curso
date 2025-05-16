prompt_lugar = "Qual lugar do mundo você iria? "
prompt_nome = "Qual seu nome? "
resposta ={}
ativa = True

while ativa:
    nome = input(prompt_nome)
    lugar = input(prompt_lugar)

    resposta[nome] = lugar

    repetir = input("Gostaria de participar da pesquisa? (sim/nao)")
    repetir_corrigido = repetir.lower().strip()

    if repetir_corrigido == 'nao':
        ativa = False

for name, place in resposta.items():
    print(f"{name.title()} gostria de ir a {place.title()}")
    
