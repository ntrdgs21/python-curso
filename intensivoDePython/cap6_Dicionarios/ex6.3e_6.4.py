python = {}

python['lower()'] = 'Método que deixa um valor string com letra minúscula'
python['append()'] = 'Função do python que adciona um valor na ultima posição de uma lista'
python['del'] = 'Função que passamos quando queremos deletar um elemento de uma lista ou um par de chave valor a um dicionário'
python['insert()'] ='Função do python que nos permite inserir um elemento na lista passando a posição'
python['pop()'] = 'Finção do python que remove o ultimo elemento de uma lista'

# for chave,valor in python.items():
#     print(chave, valor)

python['sorted()'] = 'Ordena nosso dicionário em ordem alfabética'
python['keys()'] = 'Seleciona as chaves do nosso dicionário'
python['upper()'] = 'Método que deixa um valor string com letra maiuscula'
python['values()'] = 'Seleciona os valores de um dicionário'
python['sort()'] = 'Método que nos mostra quais valores estão no nosso dicionário sem duplicatas'

for chave, valor in sorted(python.items()):
    print (f"{chave} : {valor}")
