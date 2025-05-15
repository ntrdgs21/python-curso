pessoas = {
            'nathan':{
            'primeiro número':'22',
            'segundo número':'16'
            },
            'ariadne':{
             'primeiro número':'16',
             'segundo número':'11'
            },
           'marjorie':{
            'primeiro número':'05',
            'segundo número':'27'
           },
           'aisha':{
            'primeiro número':'27',
            'segundo número':'1'
           },
           'celio':{
            'primeiro número':'13',
            'segundo número':'9'
           }
           }



print("Os números favoritos de cada pessoa são:")
for chave, valor in pessoas.items(): 
    print(chave.title())
    for opcao,numeros in valor.items():
        print(opcao.title(), numeros)