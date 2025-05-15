mensagem = "\nInsira os ingredientes que o senhor que na sua pizza"
mensagem += "\nQuando quiser sair digite 'sair':\n "

while True:
    pizza = input(mensagem)
    if pizza == 'sair':
        break
    else:
        print(pizza)