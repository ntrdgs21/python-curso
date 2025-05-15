mensagem = "Insira a sua idade: "


while True:
    idade = int(input(mensagem))
    if idade < 3:
        print(f"Com {idade} anos o ingresso é gratuito")
        saida = input("Para continuar comparando digite 'continuar', se desejar sair digite 'sair' ")
        if saida == 'sair':
                break
    if idade>3 and idade<12:
        print(f"Com {idade} anos o ingresso custará 10 reais")
        saida = input("Para continuar comparando digite 'continuar', se desejar sair digite 'sair' ")
        if saida == 'sair':
                break
    if idade>12:
        print(f"Com {idade} anos o ingresso custará 15 reais")
        saida = input("Para continuar comparando digite 'continuar', se desejar sair digite 'sair' ")
        if saida == 'sair':
            break
    else:
        print("Valor inválido, deseja sair?")
        sair = input("Para sair digite sair: ")
        if sair == 'sair':
            break

