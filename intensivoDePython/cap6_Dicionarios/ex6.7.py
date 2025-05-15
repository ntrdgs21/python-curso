pessoas = []
clientes = {
    'cliente1':{
    'primeiro_nome': 'nathan', 
    'sobrenome': 'rodrigues', 
    'idade': '23', 
    'cidade': 'rio de janeiro'
    },
    'cliente2':{
    'primeiro_nome': 'ariadne', 
    'sobrenome': 'frança', 
    'idade': '22', 
    'cidade': 'são luís'
    },
    'cliente3':{
    'primeiro_nome': 'marjorie', 
    'sobrenome': 'farias', 
    'idade': '50', 
    'cidade': 'rio de janeiro'
    }    
    }

pessoas.append(clientes)

for grupo in pessoas:
    for identificador, dados in grupo.items():
        nome = f"{dados['primeiro_nome'].title()} {dados['sobrenome'].title()}"
        idade = dados['idade']
        cidade = dados['cidade'].title()
        print(f"{identificador}: {nome}, {idade} anos, cidade natal: {cidade}")