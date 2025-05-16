respostas = {}

# definimos uma flag 
ativa = True

while ativa:
    nome = input("Insira seu nome: ")
    carro = input("Qual carro você gostaria de comprar? ")
    
    respostas[nome] = carro  
    
    repita = input("Mais alguém responderá? (sim/nao) ")
    if repita == 'nao':
        ativa = False

for nome, carro in respostas.items():
    print(f"{nome.title()} gostaria de comprar um {carro}")