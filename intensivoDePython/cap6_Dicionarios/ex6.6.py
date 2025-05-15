pessoas = {'nathan':'python','ariadne':'java','marjorie':'javascript','aisha':'rust','celio':'python'}
pessoas['isiah'] = 'c#'
pessoas['maria'] = 'cobol'

if pessoas:
    for pessoa, linguagem in pessoas.items():
        print(f"{pessoa.title()} : {linguagem}")
    print("Obrigado a todos que participaram da pesquisa")
else:
    ("Te convido a participar de nossa pesquisa")