nomes = ["admin", "nathan", "ariadne", "júnior", "joão", "marjorie"]


if nomes:
    for nome in nomes:
        if nome == "admin":
            print(f"Olá administrador, gostaria de ver um relatório de status? ")
        else:
            print(f"Olá {nome.title()}, bem vindo!")