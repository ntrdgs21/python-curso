convidados= ["Jesus", "Paulo", "Davi","Salomão"]

# print(f"{convidados[0]}, por favor venha jantar comigo idependente dos meus erros. Preciso ouvir o senhor.")
# print(f"{convidados[1]}, venha ao meu jantar, necessito aprender com o senhor.")
# print(f"{convidados[2]}, te convido para um jantar muito especial")
# print(f"{convidados[3]}, te convido para um jantar muito especial")

print(f"{convidados[3]}, não poderá comparecer no jantar!")

convidados.pop(3)
convidados.append("Isaias")
print(f"{convidados[3]}, te convido para um jantar muito especial")

convidados.insert(1,"Pedro")
convidados.insert(2,"João")
convidados.insert(3,"Abraão")

print(f"{convidados[0]}, te convido para um jantar muito especial")
print(f"{convidados[1]}, te convido para um jantar muito especial")
print(f"{convidados[2]}, te convido para um jantar muito especial")
print(f"{convidados[3]}, te convido para um jantar muito especial")
print(f"{convidados[4]}, te convido para um jantar muito especial")

print("Remova algumas, a mesa não chegará a tempo do jantar")
print(convidados)
convidados.pop()
convidados.pop()
convidados.pop()
convidados.pop()

print(convidados)

del convidados[2]
del convidados [1]
print(convidados)

len(convidados)