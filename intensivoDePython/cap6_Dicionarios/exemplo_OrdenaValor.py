carro = {'motor':'ap 2.0', 'cambio': 'manual 6 marchas', 'marca': 'toyota', 'modelo' : 'supra A70'}
print(f"O carro {carro['modelo']} segue as seguintes especificações:")
for pecas in carro.values():
	if pecas.lower() != 'toyota' and pecas.lower() != 'supra a70':
		print(pecas)