# pessoas = {'nathan':'22','ariadne':'16','marjorie':'5','aisha':'27','celio':'13'}
# for nome in sorted(pessoas.keys()):
# 	print(f"{nome.title()}, obrigado por responder nossa pesquisa")

pessoas = {'nathan':'iphone','ariadne':'Samsung ','marjorie':'samsung ','aisha':'motorola','celio':'Iphone'}
print("De acordo com nossa pesquisa as marcas de celulares utilizadas na casa são; ")
marcas_normalizadas = (valor.strip().lower() for valor in pessoas.values())
for celular in set(marcas_normalizadas):
	print (celular)