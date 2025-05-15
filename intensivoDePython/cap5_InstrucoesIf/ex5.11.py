numeros = []
for numero in range(1,10):
    numeros.append(numero)

if numeros:
    for numero in numeros:
        if numero == 1:
            print (f"{numero} st")
        elif numero == 2:
            print(f"{numero} nd")
        elif numero == 3:
            print(f"{numero} rd")
        else:
            print(f"{numero} th")
