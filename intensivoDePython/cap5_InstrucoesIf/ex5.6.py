idade = int(input("Informe sua idade: "))
if idade <2:
    print("Neném")
elif idade > 2 and idade <4:
    print("Criança pequena")
elif idade >4 and idade < 13:
     print("Criança grande")
elif idade > 13 and idade < 18:
    print("Adolescente")
elif idade > 18 and idade < 65:
    print("Adulto")
elif idade>= 65:
    print("Idoso")