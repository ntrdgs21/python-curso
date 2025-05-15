tres = [valor for valor in range(1,31) if valor % 3 == 0]
print(tres)

multiplos_de_tres = []
for numeros in range(1,31):
    if numeros % 3 == 0:
        multiplos_de_tres.append(numeros)
print(multiplos_de_tres)