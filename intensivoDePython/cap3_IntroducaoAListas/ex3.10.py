cidades = ["Rio de Janeiro", "São Paulo", "Porto Alegre", "Recife", "Fortaleza", "Santa Catarina", "Coritiba", "Brasília", "Belo Horizonte"]
print(cidades	)
cidades.append("João Pessoa")
cidades.pop()
cidades.remove("Recife")

print(cidades)

cidades.sort()
print(cidades)

cidades_inverso = sorted(cidades, reverse=True)
print(cidades_inverso)

del cidades[5]

print(cidades)

numeroDeCidades= len(cidades)
print(numeroDeCidades)