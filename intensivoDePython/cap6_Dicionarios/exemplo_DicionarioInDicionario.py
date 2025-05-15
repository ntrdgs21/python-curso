carros = {
'rx7':{
'marca':'mazda',
'motor': 'v8 turbo',
'cambio': 'manual 6 marchas'
},
'corolla gr':{
'marca':'toyota',
'motor': '1.6 6 cilindros',
'cambio': 'manual 6 marchas'
},
'civic':{
'marca':'honda',
'motor': '2.0 ap',
'cambio': 'automatico cvt'
},
}
for chave, valor in carros.items():
	print(f"\nModelo: {chave.title()}")
	for chave,valor in valor.items():
	    print(f"{chave} = {valor}")