carro = {'motor':'ap 2.0', 'cambio': 'manual 6 marchas'}
print(carro['motor'])
print(carro['cambio'])

motorizacao = carro['motor']
print(f"O motor usado nesse carro é o {motorizacao}")

print(carro)
carro['marca'] = 'toyota'
carro['modelo'] = 'supra A70'
print(carro)

carro['motor'] = 'v6'
print(carro)

if carro['motor'] == 'v6':
    print(f"Esse carro com motor {carro['motor']} anda muito, porém tem um alto consumo de gasolina")
elif carro['motor'] == 'ap 2.0':
    print(f"O motor desse carro é confiável e tem um bom consulmo")
else:
    print("Me diz qual o motor dele")

del carro['cambio']
print(carro)

body_kit = carro.get('body kit', 'Não há modificações visuais no carro')
print(body_kit)

carro = {'motor':'ap 2.0', 'cambio': 'manual 6 marchas', 'marca': 'toyota', 'modelo' : 'supra A70'}
# print("segue as especificações do carro")
# for chave, valor in carro.items():
#     # print(f"\nChave {chave}")
#     # print(f"Valor: {valor}")
#     print(f"{chave} : {valor}")

print("segue as especificações do carro")
for chave in carro.keys():
	  print(chave)